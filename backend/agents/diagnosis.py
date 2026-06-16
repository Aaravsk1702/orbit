import json
from services.gemini_service import generate_response


def diagnosis_agent(report_text, feedback=""):

    prompt = f"""
    You are a medical assessment AI.

    Report:
    {report_text}

    Previous Feedback:
    {feedback}

    Return ONLY JSON:

    {{
        "possible_condition":"",
        "evidence":[""],
        "recommendation":"",
        "confidence":0
    }}

    Do not provide a definitive diagnosis.
    """

    response = generate_response(prompt)

    try:
        return json.loads(response)
    except:
        return {
            "possible_condition": "Unknown",
            "evidence": [],
            "recommendation": "Consult a doctor",
            "confidence": 50
        }