from fastapi.testclient import TestClient
from ..main import app


access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlbWFpbEBnbWFpbC5jb20iLCJleHAiOjE2MjQ1NzU3MTl9.lxk5Eo9hXyiaOR1EmypqrXQOyBGg2GWGtAxD2N3uw8s"


client = TestClient(app)


def test_create_blog_without_login():
    response = client.post(
        "/blog/", json={"title": "new blog title", "body": "new blog post"}
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Not authenticated"}


def test_create_blog_with_login():
    response = client.post(
        "/blog/",
        headers={"Authorization": f"bearer {access_token}"},
        json={"title": "new blog title", "body": "new blog post"},
    )
    assert response.status_code == 201
    assert response.json() == {
        "title": "new blog title",
        "body": "new blog post",
        "id": 15,
        "user_id": 1,
    }
