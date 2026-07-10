from sqlalchemy import create_engine
from app.core.config import settings
import urllib.parse  

safe_password = urllib.parse.quote_plus(settings.DB_PASSWORD)

DATABASE_URL = (
    f"mysql+pymysql://"
    f"{settings.DB_USER}:"
    f"{safe_password}@"
    f"{settings.DB_HOST}:"
    f"{settings.DB_PORT}/"
    f"{settings.DB_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    echo=False
)

