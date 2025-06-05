from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class EventAttendee(Base):
    __tablename__ = "event_attendee"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("event.id"), nullable=False)
    attendee_id = Column(Integer, ForeignKey("attendee.id"), nullable=False)

    event = relationship("Event", back_populates="registrations")
    attendee = relationship("Attendee", back_populates="registrations")