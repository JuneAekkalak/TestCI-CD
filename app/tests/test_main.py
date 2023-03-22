from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World1"}

def test_get_main():
    response = client.get("/callname/june")
    assert response.status_code == 200
    assert response.json() == {'hello': 'june'}

def test_post_main():
    response = client.post("/callname")
    assert response.status_code == 200
    assert response.json() == {'hello': 'june'}
