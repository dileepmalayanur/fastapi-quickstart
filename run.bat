CALL pip install -r requirements.txt
CALL alembic upgrade head
CALL set UVICORN_PORT=7005
CALL uvicorn main:app --reload
