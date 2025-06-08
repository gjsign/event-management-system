from fastapi import APIRouter, Depends, Query, Path
from sqlalchemy.orm import Session

from app.controllers.event_controller import get_upcoming_events, create_event
from app.controllers.attendee_controller import register_attendee, get_event_attendees
from app.schemas.event import EventCreate
from app.schemas.event import EventCreate, EventOut
from app.schemas.attendee import AttendeeCreate, AttendeeOut
from app.core.database import get_db

router = APIRouter()

@router.get("/", response_model=list[EventOut])
def list_events(db: Session = Depends(get_db), user_timezone: str = Query("Asia/Kolkata")):
    return get_upcoming_events(db, user_timezone)

@router.post("/", response_model=EventOut)
def create(event: EventCreate, db: Session = Depends(get_db)):
    return create_event(db, event)