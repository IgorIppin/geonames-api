from sqlalchemy import exc

from geonames_api.infra.database import logger
from geonames_api.infra.database.repositories.interfaces import (
    UserInterface, DetailInterface)

from geonames_api.infra.database.models import (
    User as UserModel, Detail as DetailModel)
from geonames_api.domain.entities.user_entity import User as UserEntity
from geonames_api.domain.entities.datail_entity import Detail as DetailEntity


class UserRepo(UserInterface):
    def __init__(self, session, auto_commit=True):
        self.session = session
        self.auto_commit = auto_commit

    def create_user(self, user: UserEntity) -> UserEntity:
        try:
            logger.debug("Init create user: {}".format(user))
            user_model = UserModel(name=user.name)
            self.session.add(user_model)
            self.session.flush()
            if self.auto_commit:
                self.session.commit()
            logger.debug("Created user with name: {}".format(user.name))
        except exc.SQLAlchemyError as e:
            logger.error("SQLalchemy exception: {}".format(e))
            raise e
        except Exception as e:
            logger.error("Unspected error: {}".format(e))
            raise e

        return UserEntity(name=user_model.name)


class DetailRepo(DetailInterface):
    def __init__(self, session, auto_commit=True):
        self.session = session
        self.auto_commit = auto_commit

    def create_detail(self, detail: DetailEntity) -> DetailEntity:
        try:
            logger.debug("Init create detail with data: {}".format(detail))
            detail_model = DetailModel(
                id=detail.id,
                zip_code=detail.zip_code,
                city=detail.city,
            )
            self.session.add(detail_model)
            self.session.flush()
            if self.auto_commit:
                self.session.commit()
            logger.debug("Created detail with id: {}".format(detail.id))
        except exc.SQLAlchemyError as e:
            logger.error("SQLalchemy exception: {}".format(e))
            raise e
        except Exception as e:
            logger.error("Unspected error: {}".format(e))
            raise e

        return DetailEntity(name=detail_model.name)

