from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api import api_router
from app.core.config import settings
from app.core.events import create_start_app_handler

def get_application() -> FastAPI:

    application = FastAPI(**settings.fastapi_kwargs)

    application.add_event_handler(
        "startup",
        create_start_app_handler(),
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_router, prefix=settings.API_V1_STR)

    return application


app = get_application()
