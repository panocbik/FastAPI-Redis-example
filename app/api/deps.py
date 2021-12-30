from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError

from redis_om import NotFoundError

from app.core import security
from app.api.errors import string
from app.core.config import settings
from app.models.user import User
from app.models.token import TokenPayload


reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/oauth2/user/token"
)


def get_current_user(
    token: str = Depends(reusable_oauth2)
) -> User:
    print(token)
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=string.CREDENTIALSERROR,
        )
    try:
        user = User.find(User.pk==token_data.sub).first()
    except NotFoundError:
        raise HTTPException(
            status_code=404, 
            detail= string.USERNOTFOUND
        )
    return user


def authenticate(
    email: str, 
    password: str
) -> Optional[User]:
    user = User.find(User.email==email).first()
    if not user:
        return None
    if not security.verify_password(password, user.password):
        return None
    return user