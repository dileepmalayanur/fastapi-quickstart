import uvicorn, os
from app import routes as api_routes
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FastAPI Quickstart")

_port = os.getenv('UVICORN_PORT')
base_url = ["http://localhost:" + _port]

app.add_middleware(
    CORSMiddleware,
    allow_origins=base_url,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(api_routes.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='::', port = int(_port), log_level="info", reload=True)
    print("Started uvicorn server !")