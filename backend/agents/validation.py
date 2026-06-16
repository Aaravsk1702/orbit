import json
from backend.services.gemini_service import generate_response


def validation_agent(report_text, diagnosis):

    prompt = f"""
    You are a senior clinical reviewer.

    Your role is to independently review a medical screening assessment.

    Original Medical Report:
    {report_text}

    Diagnosis Agent Output:
    {diagnosis}

    Tasks:

      Verify whether the findings are supported by the report.
      Identify unsupported claims.
      Identify missing evidence.
      Suggest alternative possible conditions.
      Evaluate the confidence score.
      Provide constructive feedback for improvement.

    Return confidence as an integer from 0 to 100 only.
    Do not use a 1-5 scale.

    Return ONLY valid JSON:

    {{
    "validated": true,
    "feedback": "",
    "alternative_conditions": [],
    "confidence": 0
    }}

    Do not provide a final medical diagnosis.
    """

    response = generate_response(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    print("Validation Response:")
    print(response)

    try:
        return json.loads(response)
    except:
        return {
            "validated": False,
            "feedback": "Unable to validate",
            "confidence": 50
        }