from fastapi import HTTPException

import logging
import sys
from logging.config import dictConfig
from typing import Any, Optional

from geonames_api.config.settings import LogConfig


dictConfig(LogConfig().dict())
logger = logging.getLogger("exceptions")


class WarningException(HTTPException):
    def __init__(
            self,
            status_code: int,
            detail: Any = None,
            headers: Optional[dict[str, Any]] = None,
    ) -> None:
        logger.warning('status_code: %s:detail: %s:headers: %s' % (status_code, detail, headers))
        super().__init__(status_code=status_code, detail=detail, headers=headers)


class ErrorException(HTTPException):
    def __init__(
            self,
            status_code: int,
            detail: Any = None,
            headers: Optional[dict[str, Any]] = None,
    ) -> None:
        logger.error('status_code: %s:detail: %s:headers: %s' % (status_code, detail, headers))
        super().__init__(status_code=status_code, detail=detail, headers=headers)


class CriticalException(HTTPException):
    def __init__(
            self,
            status_code: int,
            detail: Any = None,
            headers: Optional[dict[str, Any]] = None,
    ) -> None:
        logger.critical('status_code: %s:detail: %s:headers: %s' % (status_code, detail, headers))
        super().__init__(status_code=status_code, detail=detail, headers=headers)
        sys.exit(detail)
