from fastapi import FastAPI, UploadFile, File
from PIL import Image
import pytesseract
import shutil

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ExamScanner AI Backend Running"}

@app.post("/scan")
async def scan_exam(file: UploadFile = File(...)):

    file_path = file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    image = Image.open(file_path)

    extracted_text = pytesseract.image_to_string(image)

    return {
        "filename": file.filename,
        "text": extracted_text
    }