from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from geonames_api.config.settings import config
from geonames_api.domain.entities import User, Detail
from geonames_api.infra.database.repositories.repositories import GameRepo, GuessRepo
from geonames_api.infra.database.orm import db
from geonames_api.domain.use_cases import ValidateCode, ValidateCodeLen

router = APIRouter()


@router.get(
    path='/',
    response_model=CurrentCityResponse
)
async def get_user_city(user_name: str, zip_code: int) -> CurrentCityResponse:
    """ Get the current game with all guesses associated with its game."""


    user: User = UserRepo(db).post_game(user_name=user_name)
    detail: Detail = DetailRepo(
        db).get_guess_by_gameid(game_id=game_id)

    if not game:
        raise HTTPException(404, detail="Game not found")
    return CurrentGameResponse(id=game.id,
                               state=game.state,
                               timestamp=game.timestamp,
                               code=game.code,
                               guess=guess_list)
