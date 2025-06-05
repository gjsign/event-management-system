from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal

from app.controllers.event_controller import get_upcoming_events, create_event
from app.schemas.event import EventCreate
from app.models.event import Event
from app.schemas.event import EventCreate, EventOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[EventOut])
def list_events(db: Session = Depends(get_db)):
    return get_upcoming_events(db)

@router.post("/", response_model=EventOut)
def create(event: EventCreate, db: Session = Depends(get_db)):
    return create_event(db, event)