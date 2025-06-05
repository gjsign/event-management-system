from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Attendee(Base):
    __tablename__ = "attendee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    registrations = relationship("EventAttendee", back_populates="attendee", cascade="all, delete-orphan")
