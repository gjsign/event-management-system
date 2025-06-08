from datetime import datetime, timedelta

class BaseTest:
    def create_event(self, client, name="Sample Event", location="Default Location", capacity=100):
        start_time = datetime.utcnow() + timedelta(days=1)
        end_time = start_time + timedelta(hours=2)

        response = client.post("/events/", json = {
            "name": name,
            "location": location,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "max_capacity": capacity
        })

        assert response.status_code == 200
        return response.json()
    
    def register_attendee(self, client, event_id, name="Test User", email="test@example.com"):
        response = client.post(f"/events/{event_id}/register", json={
            "name": name,
            "email": email
        })
        assert response.status_code == 200
        return response.json()