from datetime import datetime
from pydantic import BaseModel, Field

class ChatBotDto(BaseModel):
    title: str = Field(..., description="title BOT")
    link: str = Field(..., description="Link Sale")
    status: bool = Field(..., description="Default Status == True")
    prices: str = Field(..., description="Price")
    linkAvatar: str = Field(..., description="Avatar URL")


