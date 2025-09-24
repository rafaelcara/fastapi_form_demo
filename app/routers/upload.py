from fastapi import APIRouter, UploadFile, File
from app.config import UPLOAD_DIR
from app.utils.file_ops import save_upload_file
import os

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.post("/{protocol}")
async def test(protocol: str, pdf_file: UploadFile = File(...), xml_file: UploadFile = File(...)):
    pdf_path = UPLOAD_DIR  
    xml_path = UPLOAD_DIR  

    save_upload_file(pdf_file, pdf_path)
    save_upload_file(xml_file, xml_path)

    return {
        "protocol": protocol,
        "pdf_saved": pdf_path,
        "xml_saved": xml_path,
    }
