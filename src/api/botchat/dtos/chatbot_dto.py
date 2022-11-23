from datetime import datetime
from pydantic import BaseModel, Field

class ChatBotDto(BaseModel):
    title: str = Field(..., description="title BOT")
    link: str = Field(..., description="Link Sale")
    status: str = Field(..., description="Default Status == True")


