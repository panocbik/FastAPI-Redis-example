from typing import Text
from datetime import datetime

from pydantic import BaseModel

from redis_om import HashModel, Field
from app.core.dependencies import connect_to_db


class Task(HashModel):
    name: str = Field(index=True)
    description: Text
    status: str = "pending"
    created_at: datetime = datetime.now()

    class Meta:
        database = connect_to_db()


class PostTask(BaseModel):
    name: str
    description: str
