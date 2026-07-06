from app.agents.research_agent import research
from app.agents.summary_agent import generate_summary
from app.agents.writer_agent import generate_report
from app.agents.analysis_agent import analyze_document
from app.agents.verification_agent import verify_answer


def run_summary_agent(question: str):
    context = research(question)

    summary = generate_summary(context)

    analysis = analyze_document(context)

    verification = verify_answer(
        summary,
        context
    )

    return {
        "summary": summary,
        "analysis": analysis,
        "verification": verification
    }


def run_report_agent(topic: str):
    context = research(topic)

    report = generate_report(
        context,
        topic
    )

    analysis = analyze_document(context)

    verification = verify_answer(
        report,
        context
    )

    return {
        "report": report,
        "analysis": analysis,
        "verification": verification
    }