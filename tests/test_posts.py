import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200

def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

def test_get_nonexistent_post():
    response = requests.get(f"{BASE_URL}/posts/99999")
    assert response.status_code == 404

def test_create_post():
    new_post = {
        "title": "QA Engineering",
        "body": "Testing is important",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "QA Engineering"