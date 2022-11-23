
from api.message.entities.chatCreate import AppUser
from bson import ObjectId
import bson
from core.database.connection import db, chat_collection,mess_collection
from api.message.dtos.chat_dto import ChatDto
from datetime import datetime



class messService():
    def user_helper(self, chat) -> dict:
        return {
            "id": str(chat["_id"]),
            "botID":str(chat["botID"]),
            "userID": str(chat["userID"]),
            "message": chat["message"],
            "dateMess": chat["dateMess"],
            
        }
    def binding_user(self, datas):
        users = []
        for data in datas:
            user = {
            "id": str(data["_id"]),
            "botID":str(data["botID"]),
            "userID": str(data["userID"]),
            "message": data["message"],
            "dateMess": data["dateMess"],

            }
            users.append(user)
        return users
            
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
