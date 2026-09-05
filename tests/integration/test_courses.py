import os
from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.db import Base, get_session
from app.domain import course  # noqa: F401
from app.main import app

pytestmark = pytest.mark.skipif(
    os.getenv("RUN_INTEGRATION_TESTS") != "1",
    reason="integration tests require PostgreSQL",
)


@pytest.fixture()
def client() -> Generator[TestClient]:
    database_url = os.environ["TEST_DATABASE_URL"]
    engine = create_engine(database_url, pool_pre_ping=True)
    testing_session_local = sessionmaker(bind=engine, autoflush=False, autocommit=False)

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    def override_get_session() -> Generator[Session]:
        with testing_session_local() as session:
            yield session

    app.dependency_overrides[get_session] = override_get_session

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)
    engine.dispose()


def test_readiness_checks_database(client: TestClient) -> None:
    response = client.get("/health/ready")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_list_and_get_course(client: TestClient) -> None:
    create_response = client.post(
        "/api/v1/courses",
        json={
            "title": "Kubernetes Delivery Basics",
            "description": "Build, package, and deploy an HTTP service through GitOps.",
            "level": "beginner",
        },
    )

    assert create_response.status_code == 201
    created = create_response.json()
    assert created["title"] == "Kubernetes Delivery Basics"

    list_response = client.get("/api/v1/courses")
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1

    get_response = client.get(f"/api/v1/courses/{created['id']}")
    assert get_response.status_code == 200
    assert get_response.json()["id"] == created["id"]


def test_missing_course_returns_404(client: TestClient) -> None:
    response = client.get("/api/v1/courses/00000000-0000-0000-0000-000000000000")

    assert response.status_code == 404
