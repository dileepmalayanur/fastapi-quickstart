#!/bin/bash

pip install -r requirements.txt
export UVICORN_PORT=7005
uvicorn main:app --reload
