# Project : Anime Backend With FastAPI (REST API)

## Description
This project is a backend implementation of an anime streaming service using FastAPI. It provides a RESTful API for managing anime data, including CRUD operations for anime, genres, and users.

## Installation
Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate
```
Install the required dependencies:
```bash
pip install -r requirements.txt
```
Run the application:
```bash
uvicorn main:app --reload
```

### Phase 0: Setup and Configuration
It includes setting up the postgresql database, configuring environment variables, and initializing the application.
Describing the project structure and dependencies.
Also dockerization of the application.

### Project Structure
The project is organized into the following directories:
- `app`: Contains the main application code.
- `core`: Contains core application logic.
- `config`: Contains configuration files.
- `database`: Contains database-related code.
- `models`: Contains data models.
- `routes`: Contains route definitions.
- `v1`: Contains version 1 of the API.
- `schemas`: Contains data schemas.
- `services`: Contains business logic services.
- `repositories`: Contains data access layer code.
