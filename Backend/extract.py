from fastapi import FastAPI, File, UploadFile
from PyPDF2 import PdfReader
from docx import Document
import re

app = FastAPI()

# Function to extract text from PDF
def extract_pdf_text(file):
    reader = PdfReader(file)
    print("extract_pdf_text")
    return " ".join(page.extract_text() for page in reader.pages)

# Function to extract text from Word
def extract_docx_text(file):
    doc = Document(file)
    print("extract_docx_text")
    return " ".join(paragraph.text for paragraph in doc.paragraphs)

# Function to parse the extracted text
def parse_resume(text):
    print("parse_resume")
    data = {}
    # Extract Name (simplified using the first line as an example)
    data['name'] = text.split("\n")[0]
    # Extract Email
    email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    data['email'] = email_match.group(0) if email_match else None
    # Extract Phone
    phone_match = re.search(r'\b\d{10}\b', text)  # Simple 10-digit number
    data['phone'] = phone_match.group(0) if phone_match else None
    return data

@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):
    print("upload_resume")
    if file.content_type == "application/pdf":
        text = extract_pdf_text(file.file)
    elif file.content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text = extract_docx_text(file.file)
    else:
        return {"error": "Unsupported file type"}

    parsed_data = parse_resume(text)
    print(parsed_data)
    return parsed_data
