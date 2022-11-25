from fastapi import APIRouter, Depends, Query, UploadFile, status
from typing import List
from typing import Union
from api.payment.services.PaymentService import PaymentService
from api.payment.dtos.PaymentDto import PaymentDto
from fastapi.responses import JSONResponse
from datetime import datetime
payment_router = APIRouter()
payment_services = PaymentService()

@payment_router.post("/payment")
async def create_payment(paymentDto: PaymentDto):
    try:
        print("Creating payment")
        data = payment_services.payment_Abot(paymentDto)
        return data
        
    except Exception as e:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = { 'message' : str(e) }
            )
    
@payment_router.get("/getpaymentuser")
async def getAllUserPayment(userID: str):
    try:
        print("Get All message from bot")
        data = payment_services.allChatBotPayment(userID)
        return data
        
    except Exception as e:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = { 'message' : str(e) }
            )
@payment_router.get("/getpayment")
async def getAllPayment():
    try:
        print("Get All message from bot")
        data = payment_services.allPayment()
        return data
        
    except Exception as e:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = { 'message' : str(e) }
            )
@payment_router.put("/deletepayment")
async def deletePayment(_id: str):
    try:
        
        data = payment_services.deletePayment(_id)
        return data
        
    except Exception as e:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = { 'message' : str(e) }
            )
