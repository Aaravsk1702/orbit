from backend.services.gemini_service import generate_response


def chat_agent(
    diagnosis,
    validation,
    user_question
):

    prompt = f"""
    You are a medical follow-up assistant.

    Previous Analysis:

    Diagnosis:
    {diagnosis}

    Validation:
    {validation}

    User Question:
    {user_question}

    Answer the user's question based only on
    the previous analysis.

    Keep the answer concise.
    """

    return generate_response(prompt)