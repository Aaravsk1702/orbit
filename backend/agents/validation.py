import json
from backend.services.deepseek_service import deepseek_response


def validation_agent(report_text, diagnosis):

    prompt = f"""
    You are a senior clinical reviewer.

    Your role is to independently review a medical screening assessment.

    Original Medical Report:
    {report_text}

    Diagnosis Agent Output:
    {diagnosis}

    Tasks:

    1. Verify whether the findings are supported.
    2. Identify unsupported claims.
    3. Suggest alternative possible conditions.
    4. Evaluate the confidence score.
    5. Provide feedback

    Return ONLY valid JSON:

    {{
    "validated": true,
    "feedback": "",
    "alternative_conditions": [],
    "confidence": 0
    }}

    Confidence must be an integer from 0 to 100.
    """

    response = deepseek_response(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    print("Deepseek Validation Response:")
    print(response)

    try:
        return json.loads(response)
    
    except Exception as e:

        print("DeepSeek Parse Error:", e)
        print(response)

        return {
            "validated": False,
            "feedback": "Validation service error",
            "alternative_conditions": [],
            "confidence": 50
        }