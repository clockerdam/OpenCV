import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Resume(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    author: str = Field(...)
    synopsis: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "Don Quixote",
                "author": "Miguel de Cervantes",
                "synopsis": "..."
            }
        }