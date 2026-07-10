from pydantic import BaseModel
from datetime import datetime

class DocumentResponse(BaseModel):
    id: int
    filename: str
    filepath: str
    created_at: datetime
    created_by: int

    model_config = {
        "from_attributes": True
    }
