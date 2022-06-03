from fastapi import FastAPI
import uvicorn

from geonames_api.config.settings import config
from geonames_api.api.v1.router import v1_router

app = FastAPI(
    version="0.1.0",
    title=config.app_name,
    openapi_url=f'{config.api_prefix}/openapi.json')

app.include_router(v1_router, prefix=config.api_prefix)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=5000, reload=True)
