from fastapi import APIRouter, Depends, Query, UploadFile, status
from typing import List
from typing import Union
from api.message.messServices.messServices import messService
from api.message.dtos.chat_dto import ChatDto
from fastapi.responses import JSONResponse
from datetime import datetime
mess_router = APIRouter()
mess_services = messService()

@mess_router.post("/chatmessages")
async def create_chat(chatDto: ChatDto):
    try:
        print("Creating user")
        data = mess_services.create_mess(chatDto)
        return data
        
    except Exception as e:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = { 'message' : str(e) }
            )

