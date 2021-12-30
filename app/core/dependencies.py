from redis.client import Redis
from redis_om import get_redis_connection

from app.core.config import settings


def connect_to_db() -> Redis:
    return get_redis_connection(
        host=settings.redis_host,
        port=settings.redis_port,
        password=settings.redis_pass,
        decode_responses=True
    )
