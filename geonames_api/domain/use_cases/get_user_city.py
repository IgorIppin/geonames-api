# -*- coding: utf-8 -*-

from geonames_api.config import settings


class GetCityUseCase:
    def __int__(self, zip_code):
        self.zip_code = zip_code

    async def get_by_zip_code(self):

