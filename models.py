import uuid
from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId

class CV(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    content: str = Field(...)
    link: str = Field(...)
        