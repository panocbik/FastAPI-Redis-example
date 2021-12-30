from typing import List, Optional, Any

from fastapi import (
    APIRouter,
    Response,
    HTTPException, 
    status,
    Depends
)
from redis_om import NotFoundError

import app.api.errors.string as string
from app.api import deps
from app.models.task import Task, PostTask
from app.models.user import User


router = APIRouter()


@router.get(
    path='',
    status_code= status.HTTP_200_OK,
    summary='Informaion about all Tasks',
    response_model= List[Task]
)
async def tasks(
    name: Optional[str] = None,
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    if name is None:
        return Task.find().all()
    return Task.find(Task.name==name).all()


@router.post(
    path='',
    status_code= status.HTTP_201_CREATED,
    summary='Create new Task',
    response_model= Task
)
async def create(task: PostTask) -> Any:
    task_redis = Task(name=task.name, description=task.description)
    return task_redis.save()


@router.get(
    path='/{pk}',
    status_code= status.HTTP_200_OK,
    summary='Informaion about a specific Task',
    response_model= Task
)
async def task(pk: str) -> Any:
    try:
        task = Task.get(pk)
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=string.TASKNOTFOUND
        )
    return task


@router.put(
    path='/{pk}',
    status_code= status.HTTP_202_ACCEPTED,
    summary='Informaion about a specific Task',
    response_model= Task
)
async def update(pk: str) -> Any:
    try:
        task = Task.get(pk)
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=string.TASKNOTFOUND
        )
    task.status = 'completed'
    return task.save()


@router.delete(
    path='/{pk}',
    status_code= status.HTTP_204_NO_CONTENT,
    summary='Delete a Task'
)
async def delete(pk: str) -> Any:
    try:
        Task.get(pk).delete()
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=string.TASKNOTFOUND
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
