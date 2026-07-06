from app.services.vector_store import load_vector_store


def retrieve_context(question: str, k: int = 4):
    """
    Retrieve the most relevant chunks from the FAISS vector database.
    """

    try:
        db = load_vector_store()

        docs = db.similarity_search(
            question,
            k=k
        )

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        return context

    except Exception as e:
        print(f"RAG Error: {e}")
        return ""