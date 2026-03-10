import redis
from app.config import settings

redis_client = redis.Redis.from_url(settings.REDIS_URL)


def set_cache(key, value):
    redis_client.set(key, value, ex=300)


def get_cache(key):
    return redis_client.get(key)