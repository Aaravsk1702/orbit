from PIL import Image
from backend.services.gemini_service import model


def analyze_medical_image(image_path):

    with Image.open(image_path) as image:

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

        response = model.generate_content(
            [prompt, image]
        )

    return response.text