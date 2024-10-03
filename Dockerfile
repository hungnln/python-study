# Use official Python image as a base
FROM python:3.11-slim

# Set environment variables
ENV POETRY_VERSION=1.6.1

# Install system dependencies for mysqlclient and Poetry
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    libmariadb-dev \
    curl \
    && apt-get clean

# Install Poetry
RUN pip install --no-cache poetry=="$POETRY_VERSION"

# Set working directory
WORKDIR /app

# Copy pyproject.toml and poetry.lock to the container
#COPY pyproject.toml .
#
#COPY poetry.lock .

# Install dependencies using Poetry


# Copy the application code to the container
COPY . /app

# Copy the .env file to the container
COPY .env /app/.env

RUN poetry install --no-root --no-dev

# Copy the service account key file to the container
COPY serviceAccountKey.json /app/serviceAccountKey.json

# Expose the port the app runs on
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD ["poetry", "run", "flask", "run"]
