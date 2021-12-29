from redis.client import Redis
from redis_om import get_redis_connection

from app.core.config import get_app_settings
from app.core.settings.app import AppSettings

def connect_to_db(
    settings: AppSettings = get_app_settings()
) -> Redis:
    return get_redis_connection(
        host=settings.redis_host,
        port=settings.redis_port,
        password=settings.redis_pass,
        decode_responses=True
    )
