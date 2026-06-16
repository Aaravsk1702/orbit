import json
from services.gemini_service import generate_response


def validation_agent(report_text, diagnosis):

    prompt = f"""
    Review this medical assessment.

    Report:
    {report_text}

    Assessment:
    {diagnosis}

    Return ONLY JSON:

    {{
      "validated": true,
      "feedback":"",
      "confidence":0
    }}
    """

    response = generate_response(prompt)

    try:
        return json.loads(response)
    except:
        return {
            "validated": False,
            "feedback": "Unable to validate",
            "confidence": 50
        }