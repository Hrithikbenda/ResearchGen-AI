from app.services.rag_service import retrieve_context


def research(question: str):
    context = retrieve_context(question)
    return context