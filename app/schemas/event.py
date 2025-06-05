from datetime import datetime
from pydantic import BaseModel

class EventCreate(BaseModel):
    name: str
    location: str
    start_time: datetime
    end_time: datetime
    max_capacity: int

class EventOut(EventCreate):
    id: int
    created_at: datetime

    # class Config:
        # orm_mode = True