# Calculator API

This is a lightweight, production-ready Calculator Microservice API built with FastAPI.

## Features
- Supports add, subtract, multiply, divide
- JSON-based input/output
- Docker deployable

## Usage
### Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Run via Docker
```bash
# Build a Docker image with the API
docker build -t calculator-api .

# Run a Docker container from the image
docker run -p 8000:8000 calculator-api
```

### Example cURL

```bash
curl -X POST http://localhost:8000/calc/add -H "Content-Type: application/json" -d '{"a": 10, "b": 5}'
```

## API Endpoints

| Method | Endpoint         | Description     |
|--------|------------------|-----------------|
| POST   | `/calc/add`      | Adds two numbers|
| POST   | `/calc/subtract` | Subtracts b from a |
| POST   | `/calc/multiply` | Multiplies two numbers |
