from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from openai import OpenAI
import os

# Existing RAG Router
from app.api.rag_api import router as rag_router

# Authentication Router
from app.auth.auth_routes import router as auth_router

# Database
from app.database.database import engine
from app.database.models import Base

# ==========================
# Load Environment Variables
# ==========================
load_dotenv()

# Create Database Tables
Base.metadata.create_all(bind=engine)

# Read API Key
api_key = os.getenv("OPENROUTER_API_KEY")

print("API KEY FOUND:", api_key is not None)

# ==========================
# FastAPI App
# ==========================
app = FastAPI(
    title="ResearchGen AI",
    description="Multi-Agent AI Research & Report Generation Platform",
    version="1.0.0"
)

# ==========================
# CORS Configuration
# ==========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# OpenRouter Client
# ==========================
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# ==========================
# Include Routers
# ==========================
app.include_router(rag_router)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

# ==========================
# Home Route
# ==========================
@app.get("/")
def home():
    return {
        "message": "ResearchGen AI Backend Running"
    }


# ==========================
# Test Route
# ==========================
@app.get("/test")
def test():
    return {
        "status": "working"
    }


# ==========================
# Sample Report Generation
# ==========================
@app.get("/generate")
def generate_report(topic: str):

    print(f"\nGenerating report for: {topic}")

    prompt = f"""
Write a detailed research report on {topic}.

Sections Required:

1. Introduction
2. Key Findings
3. Challenges
4. Future Scope
5. Conclusion

Requirements:
- Minimum 1000 words
- Professional report format
- Detailed explanations
- Use headings
- Do not write poetry
- Do not summarize in a few lines
"""

    print("\n===== PROMPT SENT TO MODEL =====")
    print(prompt)
    print("================================")

    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b:free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response.choices[0].message.content

        print("\n===== MODEL RESPONSE =====")
        print(content)
        print("==========================")

        return {
            "status": "success",
            "topic": topic,
            "report": content
        }

    except Exception as e:

        print("\n===== ERROR =====")
        print(str(e))
        print("=================")

        return {
            "status": "error",
            "message": str(e)
        }