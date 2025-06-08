from fastapi import APIRouter, Depends, Path, Query
from app.controllers.attendee_controller import register_attendee, get_event_attendees
from app.schemas.attendee import AttendeeOut, AttendeeCreate
from app.core.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/{event_id}/register", response_model=AttendeeOut)
def register(event_id: int = Path(..., gt=0), attendee: AttendeeCreate = ..., db: Session = Depends(get_db)):
    return register_attendee(db, event_id, attendee)

@router.get("/{event_id}/attendees", response_model=list[AttendeeOut])
def list_attendees(event_id: int = Path(..., gt=0), 
                   skip: int = Query(0, ge=0),
                   limit: int = Query(10, le=100),
                   db: Session = Depends(get_db)):
    return get_event_attendees(db, event_id, skip=skip, limit=limit)