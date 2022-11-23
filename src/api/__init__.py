from fastapi import APIRouter


from api.user.user import user_router
from api.message.message import mess_router
router = APIRouter()

router.include_router(user_router, prefix="/api/user", tags=["User"])
router.include_router(mess_router, prefix="/api/mess", tags=["Mess"])

__all__ = ["router"]
