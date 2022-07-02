![logo](https://repository-images.githubusercontent.com/468820804/e681342b-6489-4c9f-b99f-404c7826c400)

# FastAPI Quickstart App #

Minimal FastAPI project for beginners.

- Supports caching. Install Redis for redis support.
- Supports IP rate limiting.
- Install PostgreSQL for database support (Username: postgres and Password: postgres).
- Support Encrypted JWT for login.

### Update conda package for stable version ###
```
conda config --set ssl_verify False
conda update conda
```

### Create new Python environment ###
```
conda create -n myenv python=3.10
```

### Switch to new Python environment ###
```
conda activate myenv
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Set Uvicorn Port (Windows) ###
```
set UVICORN_PORT=7005
```

### Set Uvicorn Port (Linux) ###
```
export UVICORN_PORT=7005
```

### Run command (Development) ###
```
uvicorn main:app --reload
```

### Run command (Production) ###
```
uvicorn main:app
```

### Visit URL in browser ###
```
http://localhost:7005/docs
http://localhost:7005/redoc
```

### Alembic Create Revision ###
```
alembic revision -m "created tables login, country and profile"
```

### Alembic Upgrade ###
```
alembic upgrade head
```

### Alembic Downgrade ###
```
alembic downgrade -1
```
