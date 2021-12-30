from datetime import datetime

from pydantic import BaseModel

from redis_om import HashModel, Field
from app.core.dependencies import connect_to_db


class User(HashModel):
    username: str = Field(index=True)
    email: str = Field(index=True)
    created_at: datetime = datetime.now()

    class Meta:
        database = connect_to_db()


class SelfRegister(BaseModel):
    username: str
    email: str
    password: str
