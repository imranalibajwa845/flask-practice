#!/bin/bash

echo "🚀 Starting Flask Application Setup..."

# Activate the virtual environment
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "🔹 Activating virtual environment..."
    source venv/bin/activate  # Adjust if your venv has a different name
fi

# Ensure PostgreSQL is set up before running Flask
echo "🔹 Running database setup..."
python config_db.py

# Apply migrations to ensure the latest schema
echo "🔹 Applying database migrations..."
flask db upgrade

# Export necessary environment variables
export FLASK_APP=run.py
export FLASK_ENV=development

# Start the Flask application
echo "🚀 Starting Flask server..."
flask run --host=0.0.0.0 --port=8001

echo "✅ Flask application is running on http://127.0.0.1:8001"
