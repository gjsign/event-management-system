from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.event import Event
from app.models.attendee import Attendee
from app.models.event_attendee import EventAttendee
from app.schemas.attendee import AttendeeCreate

def register_attendee(db: Session, event_id: int, attendee_data: AttendeeCreate):
    # Find event
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    # Count current registrations
    current_registrations = db.query(EventAttendee).filter(EventAttendee.event_id == event_id).count()
    if current_registrations >= event.max_capacity:
        raise HTTPException(status_code=400, detail="Event is fully booked")

    # Check if attendee exists by email, else create
    attendee = db.query(Attendee).filter(Attendee.email == attendee_data.email).first()
    if not attendee:
        attendee = Attendee(name=attendee_data.name, email=attendee_data.email)
        db.add(attendee)
        db.commit()
        db.refresh(attendee)
    else:
        # If attendee exists, check if already registered for this event
        existing_registration = db.query(EventAttendee).filter(
            EventAttendee.event_id == event_id,
            EventAttendee.attendee_id == attendee.id
        ).first()
        if existing_registration:
            raise HTTPException(status_code=400, detail="This email is already registered for the event")

    # Create registration
    registration = EventAttendee(event_id=event_id, attendee_id=attendee.id)
    db.add(registration)
    db.commit()
    db.refresh(registration)

    return attendee

def get_event_attendees(db: Session, event_id: int, skip: int = 0, limit: int = 10):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    registrations = db.query(EventAttendee).filter(EventAttendee.event_id == event_id).offset(skip).limit(limit).all()
    attendees = [reg.attendee for reg in registrations]
    return attendees
