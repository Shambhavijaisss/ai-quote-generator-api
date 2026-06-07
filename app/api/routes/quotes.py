from fastapi import APIRouter, HTTPException
from app.models.quote import (
    QuoteRequest,
    QuoteResponse,
    ALLOWED_CATEGORIES,
    ALLOWED_MOODS
)
from app.services.quote_service import QuoteService

router = APIRouter()
quote_service = QuoteService()


@router.post("/quotes", response_model=QuoteResponse)
async def generate_quotes(payload: QuoteRequest):

    if payload.category not in ALLOWED_CATEGORIES:
        raise HTTPException(
            status_code=400,
            detail="Invalid category"
        )

    if payload.mood not in ALLOWED_MOODS:
        raise HTTPException(
            status_code=400,
            detail="Invalid mood"
        )

    try:
        result = await quote_service.get_quotes(
            payload.category,
            payload.mood,
            payload.count
        )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )