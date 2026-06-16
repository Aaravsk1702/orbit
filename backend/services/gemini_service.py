import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_response(prompt: str):

    print("Calling Gemini...")

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print(f"Gemini Error: {e}")

        return """
        {
            "possible_conditions": ["Unable to analyze"],
            "evidence": [],
            "recommendations": [
                "Please retry analysis"
            ],
            "confidence": 0
        }
        """