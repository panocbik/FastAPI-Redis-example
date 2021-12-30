from typing import List, Optional, Any

from fastapi import (
    APIRouter,
    Response,
    HTTPException, 
    status,
    Depends
)
from redis_om import NotFoundError

from app.api import deps
from app.models.user import User, SelfRegister
from app.core.security import get_password_hash
from app.api.errors import string

router = APIRouter()


@router.post(
    path='/self-register',
    status_code= status.HTTP_201_CREATED,
    summary='Self register',
    response_model= User
)
async def create(user: SelfRegister) -> Any:
    try:
        User.find(User.email==user.email).all()
    except NotFoundError:
        raise HTTPException(
            status_code=400,
            detail=string.USEREXIST,
        )
    new_user = User(
        username=user.username, 
        email=user.email, 
        password=get_password_hash(user.password)
    )
    return new_user.save()



@router.get(
    path='/me',
    status_code= status.HTTP_201_CREATED,
    summary='User Info',
    response_model= User
)
async def create(
    current_user: User = Depends(deps.get_current_user)
) -> Any:
    try:
        user = User.get(current_user.pk)
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=string.TASKNOTFOUND
        )
    return user

