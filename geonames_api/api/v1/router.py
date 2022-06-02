from fastapi import APIRouter

from geonames_api.api.v1.endpoints import health, city


v1_router = APIRouter()
v1_router.include_router(health.router, prefix='/health', tags=['Health-check'])
v1_router.include_router(city.router, prefix='/city', tags=['City'])
