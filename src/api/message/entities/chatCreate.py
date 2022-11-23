from bson import ObjectId
from schematics.models import Model
from schematics.types import EmailType, StringType, DateTimeType, DecimalType
from schematics.transforms import blacklist
from datetime import datetime
import uuid
from typing import Optional
from pydantic import BaseModel, Field

class AppUser(Model):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    userID: str = Field(...) 
    message: str =  Field(...)
    dateMess: datetime = Field(...)

    
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "userID": "637e448e8105440a2aefef39",
                "message": "tamnhu",
                "dateMess": "2022-11-23T18:25:43.511+00:00",

            }
        }
        