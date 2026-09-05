from fastapi.testclient import TestClient

from app.main import app


def test_liveness_does_not_require_database() -> None:
    client = TestClient(app)

    response = client.get("/health/live")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_startup_health() -> None:
    client = TestClient(app)

    response = client.get("/health/startup")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
