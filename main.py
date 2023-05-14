import os
import uvicorn
import alembic.command

from alembic.config import Config
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from sqlalchemy.orm import Session
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from app import routes as api_routes
from app.cache.definitions import redis_cache, REDIS_CACHE_PREFIX
from app.cache.rate_limiter import limiter
from app.loader.properties import get_application_properties_value
from app.models.request.base_request import BaseRequest

# DATABASE UPDATE: Blow block of code upgrades database with DDL and DML changes.
config = Config('alembic.ini')
db_url: str = str(config.get_main_option("sqlalchemy.url"))
db_url = db_url.replace('localhost', str(os.getenv('DATABASE_HOST') or "localhost"))
config.set_main_option('sqlalchemy.url', db_url)
alembic.command.upgrade(config, 'head')

app = FastAPI(title="fastapi")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

_port: str = str(os.getenv('UVICORN_PORT'))
base_url = ["http://0.0.0.0:" + _port]
REDIS_URL = get_application_properties_value('redis-url')


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


@app.on_event("startup")
async def startup():
    redis_cache.init(
        host_url=os.environ.get("REDIS_URL", REDIS_URL),
        prefix=REDIS_CACHE_PREFIX,
        response_header="FASTAPI-Cache",
        ignore_arg_types=[Request, Session, BaseRequest]
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=base_url,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(api_routes.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=int(_port), log_level="info", reload=False)
    print("Started uvicorn server !")
