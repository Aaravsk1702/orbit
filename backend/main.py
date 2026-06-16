from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
import shutil
import os

from backend.graph import run_pipeline
from backend.services.pdf_parser import extract_text_from_pdf
from backend.services.image_parser import analyze_medical_image

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze")
async def analyze(
        file: UploadFile = File(...)
):

    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    file_ext = file.filename.lower().split(".")[-1]

    try:

        if file_ext == "pdf":

            report_text = extract_text_from_pdf(
                file_path
            )

        elif file_ext in ["png", "jpg", "jpeg"]:

            report_text = analyze_medical_image(
                file_path
            )

        else:

            return {
                "error": "Unsupported file type"
            }

        result = run_pipeline(
            report_text
        )

        return result

    finally:

        if os.path.exists(file_path):
            os.remove(file_path)