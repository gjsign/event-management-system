from tests.base import BaseTest

class TestAttendees(BaseTest):
    def test_attendee_registration(self, test_client):
        event = self.create_event(test_client)
        attendee = self.register_attendee(test_client, event["id"], name="Jacob", email="jacob@example.com")

        assert attendee["name"] == "Jacob"
        assert attendee["email"] == "jacob@example.com"

    def test_get_attendees(self, test_client):
        event = self.create_event(test_client)
        self.register_attendee(test_client, event["id"], name="Bob", email="bob@example.com")

        response = test_client.get(f"/events/{event['id']}/attendees")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert any(a["email"] == "bob@example.com" for a in data)