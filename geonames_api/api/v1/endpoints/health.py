from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = APIRouter()


class HealthStatusResponse(BaseModel):
    """Response model validation"""

    status: str = 'OK'


@router.get(
    path='/',
    response_model=HealthStatusResponse
)
async def healthcheck(
) -> JSONResponse:
    """Health check endpoint"""

    return HealthStatusResponse(status='OK')
