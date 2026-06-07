from fastapi import FastAPI

from app.api.routes.quotes import router as quote_router

app = FastAPI(
    title="AI Quote Generator API",
    version="1.0.0"
)


@app.get("/")
def health_check():
    return {
        "status": "healthy"
    }


app.include_router(
    quote_router,
    prefix="/api/v1",
    tags=["Quotes"]
)