import json
from backend.services.gemini_service import generate_response


def diagnosis_agent(report_text, feedback=""):

    prompt = f"""
    You are a medical assessment AI.

    Report:
    {report_text}

    Previous Feedback:
    {feedback}
    
    Return confidence as an integer from 0 to 100.

    Examples:
    10 = very low confidence
    50 = moderate confidence
    85 = high confidence
    95 = very high confidence

    Return ONLY JSON:

    {{
        "possible_conditions":[
            "..."
            "..."
            "..."
        ],
        "evidence":[""],
        "recommendation":"",
        "confidence":0
    }}

    Do not provide a definitive diagnosis.
    """

    response = generate_response(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    print("Diagnosis Response:")
    print(response)

    try:
        return json.loads(response)
    except:
        return {
            "possible_condition": "Unknown",
            "evidence": [],
            "recommendation": "Consult a doctor",
            "confidence": 50
        }