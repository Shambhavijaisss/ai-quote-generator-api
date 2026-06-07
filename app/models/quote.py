from pydantic import BaseModel, Field
from typing import List


ALLOWED_CATEGORIES = [
    "success",
    "business",
    "life",
    "leadership",
    "fitness",
    "coding",
    "startup"
]

ALLOWED_MOODS = [
    "motivational",
    "funny",
    "professional",
    "inspirational"
]


class QuoteRequest(BaseModel):
    category: str = Field(..., examples=["success"])
    mood: str = Field(..., examples=["motivational"])
    count: int = Field(default=1, ge=1, le=5)


from pydantic import BaseModel
from typing import List

class QuoteResponse(BaseModel):
    quotes: List[str]
    source: str