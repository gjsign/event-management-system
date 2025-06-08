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
curl --location 'http://127.0.0.1:8000/events/' \
--header 'Content-Type: application/json' \
--data '{
    "name": "World Chess Championship",
    "location": "New York Convention Center",
    "start_time": "2025-07-15T14:30:00+05:30",
    "end_time": "2025-07-15T22:30:00+05:30",
    "max_capacity": 2
}'

📌 2. List Events
curl --location --request GET 'http://127.0.0.1:8000/events/1/attendees' \
--header 'Content-Type: application/json' \
--data-raw '{
  "name": "Alice Johnson",
  "email": "alice@example.com"
}
'

📌 3. Register Attendee
curl --location 'http://127.0.0.1:8000/events/2/register' \
--header 'Content-Type: application/json' \
--data-raw '{
  "name": "nodirbek3",
  "email": "nodirbek3@gmail.com"
}
'

📌 4. List Attendees of an Event
curl -X GET "http://localhost:8000/events/1/attendees?skip=0&limit=10" \
-H "accept: application/json"
