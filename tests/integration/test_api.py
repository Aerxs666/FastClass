import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_health() -> None:
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:

        response = await client.get(
            "/health"
        )

    assert response.status_code == 200

    assert (
        response.json()["status"]
        == "ok"
    )


@pytest.mark.asyncio
async def test_chat_ok() -> None:
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:

        response = await client.post(
            "/api/v1/chat",
            json={
                "question":
                    "Explícame Pydantic"
            },
        )

    assert response.status_code == 200

    assert (
        response.json()["provider"]
        == "bootstrap-local"
    )


@pytest.mark.asyncio
async def test_chat_rejects_short_question() -> None:
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:

        response = await client.post(
            "/api/v1/chat",
            json={
                "question": "a"
            },
        )

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_chat_rejects_too_long_question() -> None:
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:

        response = await client.post(
            "/api/v1/chat",
            json={"question": "a" * 2001},
        )

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_info() -> None:
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:

        response = await client.get("/api/v1/info")

    assert response.status_code == 200

    # Contrato exacto de la guia (seccion 5)
    assert response.json() == {
        "name": "AI Knowledge Assistant",
        "version": "0.1.0",
        "environment": "development",
        "llm_enabled": False,
    }


@pytest.mark.asyncio
async def test_docs_available() -> None:
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:

        response = await client.get("/docs")

    assert response.status_code == 200
