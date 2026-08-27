from datetime import datetime
from pydantic import BaseModel

class DocumentCreate(BaseModel):
    filename: str
    file_type: str

class DocumentResponse(BaseModel):
    id: int
    filename: str
    file_type: str
    uploaded_at: datetime
    status: str

    class Config:
        from_attributes = True
        