from logging.config import dictConfig
import logging
from geonames_api.config.settings import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("database")
