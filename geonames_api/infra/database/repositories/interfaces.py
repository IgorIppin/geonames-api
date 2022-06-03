from abc import ABCMeta, abstractmethod

from geonames_api.domain.entities.user_entity import User as UserEntity
from geonames_api.domain.entities.datail_entity import Detail as DetailEntity


class UserInterface(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, session, auto_commit=True):
        raise NotImplementedError

    @abstractmethod
    def create_user(self, user: UserEntity) -> UserEntity:
        """Create a User item into DB

        Args:
            user (UserEntity):

        Raises:
            SQLAlchemyError: Db operations error
            Exception: unspected error

        Returns:
            UserEntity: The same object,
            with more db dependable data like name
        """
        raise NotImplementedError


class DetailInterface(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, session, auto_commit=True):
        raise NotImplementedError

    @abstractmethod
    def create_detail(self, detail: DetailEntity) -> DetailEntity:
        """Create a detail item into DB

        Args:
            detail (DetailEntity):

        Raises:
            SQLAlchemyError: Db operations error
            Exception: unspected error

        Returns:
            DetailEntity: The same object,
            with more db dependible data like id
        """
        raise NotImplementedError
