from app.services.redis_service import RedisService
from app.services.openai_service import OpenAIService
from app.core.config import settings
from app.utils.exceptions import OpenAIServiceError


class QuoteService:

    def __init__(self):
        self.redis_service = RedisService()
        self.openai_service = OpenAIService()

    async def get_quotes(
        self,
        category: str,
        mood: str,
        count: int
    ):

        cache_key = f"quotes:{category}:{mood}:{count}"

        cached = await self.redis_service.get(cache_key)

        if cached:
            return {
                "quotes": cached,
                "cached": True
            }

        try:

            quotes = await self.openai_service.generate_quotes(
                category,
                mood,
                count
            )

            await self.redis_service.set(
                cache_key,
                quotes,
                settings.CACHE_TTL
            )

            return {
                "quotes": quotes,
                "cached": False
            }

        except OpenAIServiceError:
            raise