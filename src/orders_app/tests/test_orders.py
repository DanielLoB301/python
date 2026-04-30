
import pytest
from fastapi.testclient import TestClient
from orders_app.api.main import app
from unittest.mock import patch
from hypothesis import given
from hypothesis import strategies as st
from hypothesis import settings, HealthCheck

from orders_app.domain.services import OrderService
from orders_app.infrastructure.memory_repository import MemoryOrderRepository

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

@pytest.mark.integration
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

def test_order_total_no_puede_superar_limite(client):
    token = get_token(client)

    response = client.post(
        "/orders/",
        json={"user_id": 1, "total": 20000.0},
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 400

@pytest.mark.parametrize(
    "total, expected_status",
    [
        (100, 200),
        (9999.99, 200),
        (10001, 400),
        (50000, 400),
    ],
)
def test_limite_total_parametrizado(client, total, expected_status):
    token = get_token(client)

    response = client.post(
        "/orders/",
        json={"user_id": 1, "total": total},
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == expected_status


def test_login_mock_token(client):
    with patch("orders_app.api.main.create_access_token") as mock_token:
        mock_token.return_value = "fake-token"

        response = client.post(
            "/token",
            data={"username": "admin", "password": "admin"},
        )

        assert response.json()["access_token"] == "fake-token"  

@given(
    st.floats(
        min_value=0.01,
        max_value=10000,
        allow_nan=False,
        allow_infinity=False,
    )
)
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
def test_total_valido_property(client, total):
    token = get_token(client)

    response = client.post(
        "/orders/",
        json={"user_id": 1, "total": float(total)},
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200


def test_service_con_memory_repo():
    repo = MemoryOrderRepository()
    service = OrderService(repo)

    order = service.create_order(1, 100)
    assert order.id == 1    