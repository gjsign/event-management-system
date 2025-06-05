from datetime import datetime
from pydantic import BaseModel, EmailStr

class AttendeeCreate(BaseModel):
    name: str
    email: EmailStr

class AttendeeOut(AttendeeCreate):
    id: int
    name: str
    email: EmailStr