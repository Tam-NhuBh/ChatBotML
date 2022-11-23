
from fastapi import APIRouter, Depends, Query, UploadFile, status
from typing import List
from typing import Union
from api.botchat.chatServices.chatServices import chatService
from api.botchat.dtos.chatbot_dto import ChatBotDto
from fastapi.responses import JSONResponse
from datetime import datetime
chat_router = APIRouter()
chat_services = chatService()

@chat_router.get("/allbot")
async def getAllBot():
    try:
        print("All bot")
        data = chat_services.get_all_Chat()
        return data
        
    except Exception as e:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = { 'message' : str(e) }
            )
