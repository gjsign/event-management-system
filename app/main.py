from fastapi import FastAPI
from app.routes.event_routes import router as event_router
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Event Management System")
app.include_router(event_router, prefix="/events", tags=["Events"])
