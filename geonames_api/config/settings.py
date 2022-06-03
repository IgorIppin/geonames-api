from pydantic import BaseSettings, BaseModel


class Settings(BaseSettings):
    app_name: str = "geonames_api"
    geonames_url: str = "http://api.geonames.org/postalCodeSearchJSON?" \
                        "postalcode={zip_code}&maxRows=10&country{country}=&username={user}"
    geonames_user: str = "igorapi"
    country: str = "ES"
    db_engine_url: str
    db_password: str
    db_user: str
    db_name: str
    db_host: str
    log_level: str
    api_prefix: str

    class Config:
        env_file = ".env.example"


config = Settings()


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "mycoolapp"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        "use_cases": {"handlers": ["default"], "level": LOG_LEVEL},
        "database": {"handlers": ["default"], "level": LOG_LEVEL},
        "entities": {"handlers": ["default"], "level": LOG_LEVEL},
        "api": {"handlers": ["default"], "level": LOG_LEVEL},
    }
