from exception import CustomeException
import sys
from fastapi import APIRouter, UploadFile, File, Form
from services.summarizer import summarize_text

router = APIRouter()

@router.post("/summarize")
async def summarize_text_endpoint(text: str = Form(...), type: str = Form(...)):
    try:
        summary_result = summarize_text(text, type)
        return summary_result
    except Exception as e:
        raise CustomeException(e, sys)