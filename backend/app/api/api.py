from .endpoints import document, chat
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(document.router)
api_router.include_router(chat.router)