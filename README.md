![fastapi-quickstart](https://github.com/dileepmalayanur/fastapi-quickstart/assets/83858483/e0430b83-4b88-47a6-a973-f576b2bf86f9)

# FastAPI Quickstart App #

Minimal FastAPI project for beginners.

- Supports caching. Install Redis for redis support.
- Supports IP rate limiting.
- Install PostgreSQL for database support (Username: postgres and Password: postgres).
- Support Encrypted JWT for login.

## When you have Docker installed
### Check IP Address of Docker network (Linux) ###
```
ifconfig
```
### Check IP Address of WSL network (Windows) ###
```
ipconfig
```
### Build docker image and start container (Linux/Windows) ###

Update the value of 'DATABASE_HOST' to docker-compose.yml file.

```
docker compose up
```

##### Verified in Docker version 23.0.5, build bc4487a

##### Verified in Docker Compose version v2.17.3

## When you do not have Docker installed

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

### Set Uvicorn Port (Linux) ###
```
export UVICORN_PORT=7005
```

### Set Uvicorn Port (Windows) ###
```
set UVICORN_PORT=7005
```

### Set (Optional) Database Host (Linux) ###
```
export DATABASE_HOST=localhost
```

### Set (Optional) Database Host (Windows) ###
```
set DATABASE_HOST=localhost
```

### Set Encryption Key used for JWT encryption (Linux) ###
```
export ONLINE_ENCRYPTION_KEY=PzU61WFfWSGSY3cc
```

### Set Encryption Key used for JWT encryption (Windows) ###
```
set ONLINE_ENCRYPTION_KEY=PzU61WFfWSGSY3cc
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
