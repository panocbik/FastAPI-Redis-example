from datetime import datetime
from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.core.config import settings
from app.api import deps
from app.core import security
from app.models.token import Token
from app.api.errors import string

router = APIRouter()


@router.post(
    path="/oauth2/user/token", response_model=Token, include_in_schema=False
)
def login_access_token(
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = deps.authenticate(
         email=form_data.username, 
         password=form_data.password
    )
    if not user:
        raise HTTPException(status_code=400, detail=string.INVALIDEMAIL)
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            user.pk, expires_delta=access_token_expires
        ),
        "token_type": "bearer",  
    }
