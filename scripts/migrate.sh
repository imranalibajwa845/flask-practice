#!/bin/bash

echo "🔄 Applying database migrations..."

# Check if the virtual environment is activated
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "⚠️  Warning: Virtual environment not activated! Please activate it first."
fi

# Run Flask migrations
flask db init
flask db migrate -m "Applying migrations"
flask db upgrade

echo "Migrations applied successfully!"
