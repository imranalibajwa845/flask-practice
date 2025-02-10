#!/bin/bash

echo "Starting Application..."

# Check if the virtual environment is activated
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "⚠️  Warning: Virtual environment not activated! Please activate it first."
fi

# Export necessary environment variables
export FLASK_APP=run.py
export FLASK_ENV=development

# Run Flask
flask run --host=0.0.0.0 --port=8001

echo "Flask application is running on http://127.0.0.1:8001"
