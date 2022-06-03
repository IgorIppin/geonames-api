from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from geonames_api.config.settings import config
from geonames_api.domain.entities import User, Detail
from geonames_api.infra.database.repositories.repositories import UserRepo, DetailRepo
from geonames_api.infra.database.orm import db

router = APIRouter()


class CurrentCityResponse(User):
    """Response model validation"""

    status: str = 'Created user!'


@router.post(
    path='/',
    response_model=CurrentCityResponse
)
async def created_user_city(name: str, zip_code: int) -> [User, Detail]:
    """ Create a  new user and details."""

    user_res: User = UserRepo(db).create_user(User(name=name))

    detail_res: Detail = DetailRepo(db).create_detail(Detail(zip_code=zip_code))

    return user_res, detail_res
