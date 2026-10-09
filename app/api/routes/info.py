from fastapi import APIRouter

from app.schemas.info import InfoResponse

router = APIRouter(
    prefix="/api/v1/info",
    tags=["info"],
)


@router.get(
    "",
    response_model=InfoResponse,
)
async def info() -> InfoResponse:
    return InfoResponse(
        name="AI Knowledge Assistant",
        version="0.1.0",
        environment="development",
        llm_enabled=False,
    )
