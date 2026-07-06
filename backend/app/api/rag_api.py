from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)
import shutil
import os
from dotenv import load_dotenv
from openai import OpenAI

from app.utils.pdf_loader import load_pdf
from app.services.vector_store import create_vector_store
from app.services.rag_service import retrieve_context
from app.models.question import QuestionRequest

from app.agents.orchestrator import (
    run_summary_agent,
    run_report_agent
)

from app.auth.dependencies import get_current_user

router = APIRouter()

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


# =========================
# Upload PDF
# =========================
@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...),
    current_user: str = Depends(get_current_user)
):
    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    documents = load_pdf(file_path)
    create_vector_store(documents)

    return {
        "status": "success",
        "message": f"{file.filename} uploaded and indexed.",
        "user": current_user
    }


# =========================
# Ask Questions from PDF
# =========================
@router.post("/ask")
async def ask_question(
    request: QuestionRequest,
    current_user: str = Depends(get_current_user)
):
    context = retrieve_context(
        request.question
    )

    prompt = f"""
Answer the question only using the context below.

Context:
{context}

Question:
{request.question}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    return {
        "question": request.question,
        "answer": answer,
        "user": current_user
    }


# =========================
# Summary Agent
# =========================
@router.post("/summary")
async def generate_summary_api(
    request: QuestionRequest,
    current_user: str = Depends(get_current_user)
):
    result = run_summary_agent(
        request.question
    )

    result["user"] = current_user

    return result


# =========================
# Report Agent
# =========================
@router.post("/report")
async def generate_report_api(
    request: QuestionRequest,
    current_user: str = Depends(get_current_user)
):
    result = run_report_agent(
        request.question
    )

    result["user"] = current_user

    return result