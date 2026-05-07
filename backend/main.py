from fastapi import FastAPI, UploadFile, File
from PIL import Image
import pytesseract
import shutil
from services.preprocess import preprocess_image
from services.question_detector import detect_questions
from services.text_cleaner import clean_text

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ExamScanner AI Backend Running"}

@app.post("/scan")
async def scan_exam(file: UploadFile = File(...)):

    file_path = file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    processed_path = preprocess_image(file_path)
    
    image = Image.open(processed_path)

    custom_config = r'--oem 3 --psm 6'
    
    extracted_text = pytesseract.image_to_string(
        image,
        config=custom_config
    )
    
    cleaned_text = clean_text(extracted_text)
    
    questions = detect_questions(cleaned_text)

    return {
    "filename": file.filename,
    "text": extracted_text,
    "cleaned_text": cleaned_text,
    "questions": questions
}