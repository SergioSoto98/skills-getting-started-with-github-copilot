def test_unregister_success(client):
    # remove an existing participant
    resp = client.delete("/activities/Chess Club/signup", params={"email": "michael@mergington.edu"})
    assert resp.status_code == 200

    get = client.get("/activities")
    assert "michael@mergington.edu" not in get.json()["Chess Club"]["participants"]


def test_unregister_missing_participant(client):
    resp = client.delete("/activities/Chess Club/signup", params={"email": "notfound@x.com"})
    assert resp.status_code == 404


def test_unregister_activity_not_found(client):
    resp = client.delete("/activities/NoActivity/signup", params={"email": "a@b.com"})
    assert resp.status_code == 404
