from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def create_vector_store(documents):
    embedding_model = get_embedding_model()

    vector_db = FAISS.from_documents(
        documents,
        embedding_model
    )

    vector_db.save_local("vector_db")
    return vector_db


def load_vector_store():
    embedding_model = get_embedding_model()

    return FAISS.load_local(
        "vector_db",
        embedding_model,
        allow_dangerous_deserialization=True
    )