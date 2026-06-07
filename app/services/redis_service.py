import redis
import json

from app.core.config import settings


class RedisService:

    def __init__(self):

        self.client = redis.Redis.from_url(
            settings.REDIS_URL,
            decode_responses=True
        )

    async def get(self, key: str):

        data = self.client.get(key)

        return json.loads(data) if data else None

    async def set(
        self,
        key: str,
        value,
        ttl: int
    ):

        self.client.setex(
            key,
            ttl,
            json.dumps(value)
        )