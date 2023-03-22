from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World1"}

def test_read_main():
    response = client.get("/callname/june")
    assert response.status_code == 200
    assert response.json() == {'hello': 'june'}
