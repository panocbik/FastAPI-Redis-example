from fastapi import APIRouter

from app.api.routes import task, login, user

api_router = APIRouter()
api_router.include_router(task.router, prefix="/tasks", tags=["Task"])
api_router.include_router(login.router)
api_router.include_router(user.router, prefix="/users", tags=["User"])
