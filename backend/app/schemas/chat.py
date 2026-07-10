from pydantic import BaseModel
from datetime import datetime

class ChatResponse(BaseModel):
    response: str

    model_config = {
        "from_attributes": True
    }
