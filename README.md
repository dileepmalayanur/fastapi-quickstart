# FastAPI Quickstart #

Minimal FastAPI project for beginners.

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
