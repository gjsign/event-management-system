# 🎉 Event Management System

A lightweight and efficient API to create events, register attendees, and manage scheduling using **FastAPI**, **SQLAlchemy**, and **SQLite**.

---

## 🚀 Features

- Create and list events
- Register attendees for events
- Prevent overbooking and duplicate registrations
- Convert datetime to user timezone
- Unit-tested with `pytest`

---

## 📦 Tech Stack

- **FastAPI** – Web framework
- **SQLAlchemy** – ORM
- **SQLite** – Lightweight DB
- **Pydantic** – Data validation
- **Pytest** – Unit testing

---

## 📁 Project Structure
event_management_system/
├── app/
│ ├── main.py
│ ├── models/
│ ├── schemas/
│ ├── controllers/
│ ├── routes/
│ └── core/
├── tests/
│ ├── test_events.py
│ ├── test_attendees.py
│ ├── conftest.py
│ └── base.py
├── requirements.txt
└── README.md
---

## 🛠️ Installation

1. **Clone the repo**

```bash
git clone https://github.com/gjsign/event-management-system.git
cd event-management-system

python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

▶️ Run the Application
uvicorn app.main:app --reload

Then open your browser at: http://127.0.0.1:8000/docs

🧪 Run Tests
pytest

🔁 Example API Usage
📌 1. Create Event
curl -X POST "http://localhost:8000/events/" \
-H "Content-Type: application/json" \
-d '{
  "title": "Sample Event",
  "description": "This is a test event.",
  "start_time": "2025-06-10T10:00:00",
  "end_time": "2025-06-10T12:00:00",
  "location": "Bangalore"
}'

📌 2. List Events
curl -X GET "http://localhost:8000/events/?user_timezone=Asia/Kolkata" -H "accept: application/json"

📌 3. Register Attendee
curl -X POST "http://localhost:8000/events/1/register" \
-H "Content-Type: application/json" \
-d '{
  "name": "John Doe",
  "email": "john@example.com"
}'

📌 4. List Attendees of an Event
curl -X GET "http://localhost:8000/events/1/attendees?skip=0&limit=10" \
-H "accept: application/json"
