def test_list_events(test_client):
    response = test_client.get("/events/")
    assert response.status_code == 200
