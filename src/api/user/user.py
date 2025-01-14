from fastapi import APIRouter, Depends, Query, UploadFile, status
from typing import List
from typing import Union
from api.user.userService.user_service import UserService
from api.user.dtos.register_dto import RegisterDto
from fastapi.responses import JSONResponse
from datetime import datetime
user_router = APIRouter()
user_services = UserService()

@user_router.post("/register")
async def create_user(registerDto: RegisterDto):
    try:
        print("Creating user")
        data = user_services.create_user(registerDto)
        return data
        
    except Exception as e:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = { 'message' : str(e) }
            )


@user_router.get('/get-all-user')
async def get_all_user():
    return user_services.get_all_user()

@user_router.put("/update/{id}")
async def update_user(id: str):
    return {"message": "User updated"}

@user_router.delete("/delete/{id}")
async def delete_user(id: str):
    return {"message": "User deleted"}

