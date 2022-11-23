from api.botchat.entities.chat import AppChat
from bson import ObjectId
import bson
from core.database.connection import db, chat_collection
from api.botchat.dtos.chatbot_dto import ChatBotDto
from datetime import datetime
from fastapi.responses import JSONResponse
from fastapi.encoders   import jsonable_encoder


class chatService():
    def chat_helper(self, chat) -> dict:
        return {
            "id": str(chat["_id"]),
            "title":str(chat["title"]),
            "link": str(chat["link"]),
            "status": chat["status"],

            
        }
    def binding_chat(self, datas):
        chats = []
        for data in datas:
            chat = {
            "id": str(data["_id"]),
            "title":str(data["title"]),
            "link": str(data["link"]),
            "status": data["status"],


            }
            chats.append(chat)
        return chats
            
    def chat_data(self, chatDto: ChatBotDto): 
        chat =  {
            "title": chatDto.botID,
            "link": chatDto.userID,
            "status": chatDto.message,
        }
        return chat
    

    
    # def create_bot(self, chatDto: ChatBotDto):

    #     data =  self.chat_data(chatDto)
        

    #     find_chat = chat_collection.find({
    #         '_id': ObjectId(chatDto.botID)
    #     }) 

    #     if find_chat:
    #         mess_collection.insert_one(dict(data))
    #         return {"message":"Chat Success","status": True}
            
    #     else:
    #         return {"message":"Bot ID is not exist!","status": False}

    def get_all_Chat(self):
        mess = chat_collection.find()
        return self.binding_chat(mess)

