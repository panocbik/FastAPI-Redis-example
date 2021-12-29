import os
from typing import Any,Dict, List

from app.core.settings.base import BaseAppSettings

class AppSettings(BaseAppSettings):
    # Base settings FastAPI
    debug: bool = False
    docs_url: str = "/swagger"
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/doc"
    title: str = "Redis Handler COCO"
    version: str = "2021.12.29.1"
    servers: List = [{"url": "http://localhost"}]
    allowed_hosts: List[str] = ["*"]
    openapi_tags= [{
        'name': 'Task',
        'description': 'Task creation and management'
        }]
    
    # Redis
    redis_host: str = os.environ["REDIS_HOST"]
    redis_port: str = os.environ["REDIS_PORT"]
    redis_pass: str = os.environ["REDIS_PASS"]
   
    class Config:
        validate_assignment = True

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
            "servers": self.servers,
            "openapi_tags": self.openapi_tags,
        }
