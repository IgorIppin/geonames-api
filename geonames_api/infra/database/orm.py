from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData

from geonames_api.infra.database import logger
from geonames_api.config.settings import config

metadata = MetaData()


def get_session_orm():
    """Get Sqlalchemy session

    Returns:
        [sqlalchemy.orm.session]: [Sqlalchemy  session]
    """
    logger.debug("Connecting to db {}".format(
        config.db_engine_url.format("secret", "secret", config.db_host, config.db_name)))
    logger.debug("Connecting to db {}".format(
        config.db_engine_url.format(config.db_user, config.db_password, config.db_host, config.db_name)))
    engine = create_engine(config.db_engine_url.format(
        config.db_user, config.db_password, config.db_host, config.db_name))

    metadata.bind = engine
    Session = sessionmaker(bind=engine)
    engine.connect()
    logger.debug("Connection successtful to DB")

    return Session()


db = get_session_orm()
