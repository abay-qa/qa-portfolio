import requests

def test_get_user_success():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200

def test_get_user_not_found():
    response = requests.get("https://jsonplaceholder.typicode.com/users/99999")
    assert response.status_code == 404


