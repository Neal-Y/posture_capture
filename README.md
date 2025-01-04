# Posture Capture App

This project is a posture capture application that consists of a Go backend, a Python AI microservice, and a database for storing user and post data.

## Project Structure

- **backend/**: Contains the Go backend code.
  - **cmd/**: Main program entry point.
  - **internal/**: Core logic including handlers, services, models, and clients.
  - **configs/**: Configuration files.

- **ai-service/**: Python AI microservice.
  - **app/**: Core logic including models, API routes, and utilities.
  - **tests/**: Test code.
  - **requirements.txt**: Python dependencies.
  - **main.py**: FastAPI main entry point.

- **database/**: Database related files.
  - **migrations/**: Database migration scripts.
  - **schema.sql**: Initial database structure.
  - **init-db.sh**: Database initialization script.

- **docs/**: Documentation.
  - **api-spec.md**: API specification document.

## Getting Started

1. Set up the database using `init-db.sh`.
2. Start the Go backend and Python AI microservice.
3. Access the API using the provided endpoints in `api-spec.md`.

## Requirements

- Go
- Python
- Docker

## License

This project is licensed under the MIT License.
