def test_signup_success(client):
    resp = client.post("/activities/Chess Club/signup", params={"email": "new@mergington.edu"})
    assert resp.status_code == 200
    assert "Signed up new@mergington.edu for Chess Club" in resp.json().get("message", "")

    get = client.get("/activities")
    assert "new@mergington.edu" in get.json()["Chess Club"]["participants"]


def test_signup_duplicate(client):
    resp = client.post("/activities/Chess Club/signup", params={"email": "michael@mergington.edu"})
    assert resp.status_code == 400


def test_signup_activity_not_found(client):
    resp = client.post("/activities/Nonexistent/signup", params={"email": "x@x.com"})
    assert resp.status_code == 404
