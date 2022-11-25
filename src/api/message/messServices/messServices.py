

from api.message.entities.chatCreate import AppUser
from bson import ObjectId
import bson
from core.database.connection import db, chat_collection,mess_collection
from api.message.dtos.chat_dto import ChatDto
from datetime import datetime
from fastapi.responses import JSONResponse
from fastapi.encoders   import jsonable_encoder


class messService():
    def user_helper(self, chat) -> dict:
        return {
            "id": str(chat["_id"]),
            "botID":str(chat["botID"]),
            "userID": str(chat["userID"]),
            "message": chat["message"],
            "dateMess": chat["dateMess"],
            
        }
    def binding_chat(self, datas):
        chats = []
        for data in datas:
            chat = {
            "id": str(data["_id"]),
            "botID":str(data["botID"]),
            "userID": str(data["userID"]),
            "message": data["message"],
            "dateMess": data["dateMess"],

            }
            chats.append(chat)
        return chats
            
    def chat_data(self, chatDto: ChatDto): 
        chat =  {
            "botID": chatDto.botID,
            "userID": chatDto.userID,
            "message": chatDto.message,
            "dateMess": chatDto.dateMess,

        }
        return chat
    

    
    def create_mess(self, chatDto: ChatDto):

        data =  self.chat_data(chatDto)
        

        find_chat = chat_collection.find({
            '_id': ObjectId(chatDto.botID)
        }) 

        if find_chat:
            mess_collection.insert_one(dict(data))
            return {"message":"Chat Success","status": True}
            
        else:
            return {"message":"Bot ID is not exist!","status": False}
    def get_all_messAChat(self, chatID: str):

        find_chat = chat_collection.find({
            '_id': ObjectId(chatID)
        }) 

        if find_chat:
            mess = mess_collection.find({'botID': ObjectId(chatID)})
            return self.binding_chat(mess)
            
        else:
            return {"message":"Bot ID is not exist!","status": False}