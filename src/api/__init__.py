from fastapi import APIRouter


from api.user.user import user_router
from api.message.message import mess_router
from api.botchat.botchat import chat_router
router = APIRouter()

router.include_router(user_router, prefix="/api/user", tags=["User"])
router.include_router(mess_router, prefix="/api/mess", tags=["Mess"])
router.include_router(chat_router, prefix="/api/chat", tags=["ChatBot"])
__all__ = ["router"]
