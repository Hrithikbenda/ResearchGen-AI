def analyze_document(context: str):

    words = context.split()

    word_count = len(words)

    lines = context.split("\n")

    line_count = len(lines)

    return {
        "word_count": word_count,
        "line_count": line_count,
        "preview": context[:500]
    }