from bson import ObjectId
from schematics.models import Model
from schematics.types import EmailType, StringType, DateTimeType, DecimalType
from schematics.transforms import blacklist
from datetime import datetime
import uuid
from typing import Optional
from pydantic import BaseModel, Field

class AppPayment(Model):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    paymentID: str = Field(default_factory=uuid.uuid4, alias="paymentID")
    userID: str =  Field(...)
    botID: datetime = Field(...)
    dateBought: datetime = Field(...)
    dateSale: datetime = Field(...)
    price: float = Field(...)
    paymentMethod: str = Field(...)
    status: bool= Field(...)
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "paymentID": "637e448e8105440a2aefef39",
                "userID": "tamnhu",
                "botID": "637e448e8105440a2aefef39",
                "dateBought": "2022-11-23T18:25:43.511+00:00",
                "dateSale": "2022-11-23T18:25:43.511+00:00",
                "price": "2000",
                "paymentMethod": "Paypal",
                "status": "True",
            }
        }
        