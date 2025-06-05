from sqlalchemy.orm import Session
from app.models.event import Event
from zoneinfo import ZoneInfo

from app.schemas.event import EventCreate

def get_upcoming_events(db: Session, user_timezone: str):
    utc = ZoneInfo("UTC")
    tz = ZoneInfo(user_timezone)
    events = db.query(Event).all()
    for event in events:
        event.start_time = event.start_time.replace(tzinfo=utc).astimezone(tz)
        event.end_time = event.end_time.replace(tzinfo=utc).astimezone(tz)
    return events

def create_event(db: Session, event: EventCreate):
    db_event = Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event