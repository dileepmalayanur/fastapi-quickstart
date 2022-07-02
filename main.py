from fastapi import FastAPI
import uvicorn, os
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from sqlalchemy.orm import Session
from starlette import status

from app.cache.definitions import redis_cache, REDIS_CACHE_PREFIX
from app.cache.rate_limiter import limiter
from starlette.requests import Request
from starlette.responses import JSONResponse

from app import routes as api_routes
from fastapi.middleware.cors import CORSMiddleware
from app.loader.properties import get_application_properties_value
from app.models.request.base_request import BaseRequest

app = FastAPI(title="fastapi")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

_port = os.getenv('UVICORN_PORT')
base_url = ["http://127.0.0.1:" + _port]
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
    uvicorn.run("main:app", host='0.0.0.0', port=int(_port), log_level="info", reload=True)
    print("Started uvicorn server !")
