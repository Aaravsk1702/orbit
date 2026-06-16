from PIL import Image
from backend.services.gemini_service import model


def analyze_medical_image(image_path):

    prompt = """
    You are a medical imaging assistant.

    Analyze this medical image.

    Return:
    - Findings
    - Possible abnormalities
    - Possible conditions
    - Confidence score

    Do not provide a final diagnosis.
    """

    try:  
        with Image.open(image_path) as image:
                
            response = model.generate_content(
                [prompt, image]
            )

            return response.text

    except Exception as e:
        print("Image Analysis Error:", e)

        return """
        Medical image analysis temporarily unavailable.

        Please try again later.
        """