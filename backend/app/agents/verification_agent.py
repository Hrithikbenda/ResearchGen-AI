def verify_answer(answer: str, context: str):

    score = 0

    if len(answer) > 50:
        score += 50

    if any(
        word.lower() in context.lower()
        for word in answer.split()
    ):
        score += 50

    return {
        "confidence_score": score,
        "verified": score >= 50
    }