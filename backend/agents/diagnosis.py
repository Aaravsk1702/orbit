import json
from backend.services.gemini_service import generate_response


def diagnosis_agent(report_text, patient_notes="", feedback=""):

    prompt = f"""
    You are a medical screening assistant.

    Patient Notes:
    {patient_notes}

    Medical Report:
    {report_text}

    Previous Feedback:
    {feedback}
    

    Tasks:

    1. Extract findings.
    2. Identify abnormalities.
    3. List possible conditions.
    4. Provide supporting evidence.
    5. Suggest recommendations.
    6. Return confidence from 0 to 100.


    IMPORTANT:
    - Return ONLY valid JSON.
    - Do not wrap the JSON in markdown.
    - Do not use ```json blocks.
    - Confidence must be an integer between 0 and 100.
    - possible_conditions must be a list.
    - evidence must be a list.
    - recommendations must be a list.

    Confidence Guidelines:

    95 = Strong evidence
    80 = Moderate evidence
    60 = Limited evidence
    30 = Weak evidence

Never return 100 unless findings are unequivocal and directly visible.

    Return ONLY valid JSON.

    {{
        "possible_conditions": [
            "...",
            "...",
            "..."
        ],

        "evidence": [
            "...",
            "..."
        ],

        "recommendations": [
            "...",
            "..."
        ],

        "confidence": 0
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
            "possible_condition": ["Unknown"],
            "evidence": [],
            "recommendation": ["Consult a healthcare professional"],
            "confidence": 50
        }