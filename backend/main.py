from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
import shutil

from graph import run_pipeline
from services.pdf_parser import extract_text_from_pdf

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

    report_text = extract_text_from_pdf(
        file_path
    )

    result = run_pipeline(
        report_text
    )

    return result