from bson import ObjectId
from schematics.models import Model
from schematics.types import EmailType, StringType, DateTimeType, DecimalType
from schematics.transforms import blacklist

import uuid
from typing import Optional
from pydantic import BaseModel, Field

class AppChat(Model):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...) 
    link: str =  Field(...)
    status: bool = Field(True)
    prices: str = Field(..., description="Price")
    linkAvatar: str = Field(..., description="Avatar URL")
    
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "title": "tamnhu",
                "link": "tamnhu@hcmute.com",
                "prices": "10000",
                "linkAvatar":"tamnhu@hcmute.com"
            }
        }
        