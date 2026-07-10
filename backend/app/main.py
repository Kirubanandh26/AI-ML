from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from app.db.engine import engine
from fastapi import FastAPI
from app.api.api import api_router
from app.core.config import settings

app=FastAPI(title=settings.PROJECT_NAME, 
openapi_url=f"/{settings.PROJECT_NAME}/openapi.json", docs_url=settings.API_DOC_PATH)

app.include_router(api_router, prefix=f"/{settings.PROJECT_NAME}")