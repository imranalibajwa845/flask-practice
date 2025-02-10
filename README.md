# Flask Practice App

This is a Flask practice project to learn and implement Flask, PostgreSQL, and related technologies.

## How to Run the Application

```bash
# Clone the Repository
git clone https://github.com/yourusername/flask-practice.git
cd flask-practice

# Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install Dependencies
pip install -r requirements.txt

# Set Up the Database
python config_db.py

# Apply Database Migrations
flask db upgrade

# Run the Application
.scripts/run.sh  # Linux/macOS
python run.py  # Windows

# The app should now be running at http://127.0.0.1:80001
```
