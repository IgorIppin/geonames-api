# -*- coding: utf-8 -*-

from fastapi import status
from httpx import AsyncClient, Response, ConnectError, ReadTimeout

from geonames_api.config import settings
from geonames_api.config.exceptions import WarningException, ErrorException
from geonames_api.domain.entities import Detail


class CityRepo:
    @staticmethod
    async def get_by_zip_code(zip_code: int) -> Detail:
        try:
            async with AsyncClient() as client:
                response: Response = await client.get(
                    url=settings.config.geonames_url.format(
                        zip_code=zip_code,
                        country=settings.config.country,
                        user=settings.config.geonames_user,

                    )
                )
                if response.status_code != status.HTTP_200_OK:
                    raise WarningException(
                        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                        detail=[{
                            'loc': ['external'],
                            'msg': f'There was an error on external services. core: {response.status_code}',
                            'type': 'external_service_error',
                        }]
                    )

                return Detail(**response.json().get('data')) if response.json().get('found') else {}
        except ReadTimeout:
            raise WarningException(
                status_code=status.HTTP_408_REQUEST_TIMEOUT,
                detail=[{
                    'loc': ['external'],
                    'msg': 'There was an error on external services. geonames.org: timeout',
                    'type': 'external_service_error',
                }]
            )
        except ConnectError:
            raise ErrorException(
                status_code=status.HTTP_504_GATEWAY_TIMEOUT,
                detail=[{
                    'loc': ['external'],
                    'msg': 'There was an error on external services. geonames.org: unreachable',
                    'type': 'external_service_error',
                }]
            )
