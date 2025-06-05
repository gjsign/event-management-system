from sqlalchemy.orm import Session
from app.models.event import Event

from app.schemas.event import EventCreate

def get_upcoming_events(db: Session):
    return db.query(Event).all()

def create_event(db: Session, event: EventCreate):
    db_event = Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event