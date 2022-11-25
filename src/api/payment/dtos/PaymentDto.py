from datetime import datetime
from pydantic import BaseModel, Field

class PaymentDto(BaseModel):
    paymentID: str = Field(..., description=" paymentID")
    userID: str = Field(..., description="Username")
    botID: str = Field(..., description="Password")
    dateBought: datetime = Field(..., description="dateBought")
    dateSale: datetime =  Field(..., description="dateSale")
    price: float =  Field(..., description="Price")
    paymentMethod: str = Field(..., description='Payment Method')
    status: bool = Field(..., description='Status')