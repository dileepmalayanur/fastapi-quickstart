# Using official python runtime base image
FROM python:3.10.11-slim

LABEL authors="Dileep Malayanur"

# Update base image with latest fixes
RUN apt-get update \
    && apt-get install -y --no-install-recommends

# Creates a directory named app and changes to the same
WORKDIR /app

# Copy code from the current folder to /app inside the container
COPY .. .

# Update pip
RUN pip install --upgrade pip

# Install application dependencies
RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0"]
