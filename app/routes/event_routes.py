from fastapi import APIRouter, Depends, Query, Path
from sqlalchemy.orm import Session
from app.core.database import SessionLocal

from app.controllers.event_controller import get_upcoming_events, create_event
from app.controllers.attendee_controller import register_attendee, get_event_attendees
from app.schemas.event import EventCreate
from app.models.event import Event
from app.schemas.event import EventCreate, EventOut
from app.schemas.attendee import AttendeeCreate, AttendeeOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[EventOut])
def list_events(db: Session = Depends(get_db), user_timezone: str = Query("Asia/Kolkata")):
    return get_upcoming_events(db, user_timezone)

@router.post("/", response_model=EventOut)
def create(event: EventCreate, db: Session = Depends(get_db)):
    return create_event(db, event)

@router.post("/{event_id}/register", response_model=AttendeeOut)
def register(event_id: int = Path(..., gt=0), attendee: AttendeeCreate = ..., db: Session = Depends(get_db)):
    return register_attendee(db, event_id, attendee)

@router.get("/{event_id}/attendees", response_model=list[AttendeeOut])
def list_attendees(event_id: int = Path(..., gt=0), 
                   skip: int = Query(0, ge=0),
                   limit: int = Query(10, le=100),
                   db: Session = Depends(get_db)):
    return get_event_attendees(db, event_id, skip=skip, limit=limit)