
from exception import CustomeException

import sys

from fastapi import APIRouter, Request, Form

from services.summarization_service import summarize_text


router = APIRouter()


@router.post("/summarize")
async def summarize_text_endpoint(
    request: Request,
    text: str = Form(...),
    type: str = Form(...)
):

    try:

        # Get the ModelManager created during FastAPI startup
        model_manager = request.app.state.model_manager

        # Use already-loaded model
        summary_result = summarize_text(
            text,
            type,
            model_manager
        )

        return summary_result

    except Exception as e:

        raise CustomeException(e, sys)

