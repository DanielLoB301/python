from fastapi.testclient import TestClient
from orders_app.api.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200

def get_token(client):
    response = client.post(
        "/token",
        data={"username": "admin", "password": "admin"},
    )
    return response.json()["access_token"]


def test_create_order(client):
    token = get_token(client)

    response = client.post(
        "/orders/",
        json={"user_id": 1, "total": 100.0},
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 100.0


def test_list_orders(client):
    token = get_token(client)

    client.post(
        "/orders/",
        json={"user_id": 1, "total": 200.0},
        headers={"Authorization": f"Bearer {token}"},
    )

    response = client.get(
        "/orders/",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert len(response.json()) == 1    