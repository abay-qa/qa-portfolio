import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200

def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"

def test_get_nonexistent_user():
    response = requests.get(f"{BASE_URL}/users/99999")
    assert response.status_code == 404

def test_create_user():
    new_user = {
        "name": "Abay Ergaliev",
        "username": "abay-qa",
        "email": "ergaliev@gmail.com"
    }
    response = requests.post(f"{BASE_URL}/users", json=new_user)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Abay Ergaliev"