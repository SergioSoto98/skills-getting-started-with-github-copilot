def test_get_activities_contains_chess_club(client):
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    assert "Chess Club" in data
    assert "participants" in data["Chess Club"]
    assert "michael@mergington.edu" in data["Chess Club"]["participants"]
    assert "daniel@mergington.edu" in data["Chess Club"]["participants"]
