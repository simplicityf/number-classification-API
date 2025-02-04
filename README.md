# Number Classification API

A Flask-based API that classifies numbers with mathematical properties and fetches a fun fact.

## Features
- Checks if a number is **prime, perfect, or Armstrong**.
- Identifies if the number is **odd or even**.
- Computes the **digit sum**.
- Fetches a **fun fact** from NumbersAPI.
- Returns results in **JSON format**.

## API Endpoint
**GET** `/api/classify-number?number=<integer>`

### Example Request
```bash
curl "https://your-deployed-api.com/api/classify-number?number=371"
```

# Getting Started

Set up virtual environment (Note: This is on windows)
```
python -m venv venv
venv/Scripts/activate
``` 

To install the dependencies
```
pip install -r requirements.txt
```

To run the app
```
flask --app app --debug run
```