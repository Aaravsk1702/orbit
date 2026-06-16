from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
from fastapi import Form
import shutil
import os

from backend.graph import run_pipeline
from backend.services.report_generator import generate_report
from backend.services.pdf_parser import extract_text_from_pdf
from backend.services.image_parser import analyze_medical_image

from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def home():

    return FileResponse(
        "frontend/index.html"
    )

@app.get("/download-report")
def download_report():

    return FileResponse(
        path="orbit_report.pdf",
        media_type="application/pdf",
        filename="orbit_report.pdf"
    )

@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    patient_notes: str = Form("")
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
            report_text,
            patient_notes
        )

        if "diagnosis" in result and "validation" in result:

            report_path = generate_report(
                file.filename,
                patient_notes,
                result["diagnosis"],
                result["validation"]
            )

            result["report_file"] = report_path

        return result

    finally:

        try:
            if os.path.exists(file_path):
                os.remove(file_path)

        except Exception as e:
            print("File Cleanup Error:", e)