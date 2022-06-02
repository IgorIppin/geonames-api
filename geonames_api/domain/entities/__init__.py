import logging
from logging.config import dictConfig

from geonames_api.domain.entities.datail_entity import Detail
from geonames_api.domain.entities.user_entity import User
from geonames_api.config.settings import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("entities")
