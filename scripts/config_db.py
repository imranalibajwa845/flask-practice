import psycopg2
from psycopg2 import sql
import os

# Database connection details
DB_HOST = "localhost"
DB_PORT = "5432"
DB_ADMIN_USER = "postgres"  # Change if necessary
DB_ADMIN_PASSWORD = "your_admin_password"  # Change to your actual password
DB_NAME = "flask_practice"
DB_USER = "app_user"
DB_USER_PASSWORD = "app_password"

# Function to connect as PostgreSQL admin
def connect_as_admin():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user=DB_ADMIN_USER,
            password=DB_ADMIN_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True
        return conn
    except Exception as e:
        print(f"❌ Error connecting as admin: {e}")
        exit(1)

# Function to check if a role exists
def role_exists(cursor, role_name):
    cursor.execute(sql.SQL("SELECT 1 FROM pg_roles WHERE rolname = %s;"), [role_name])
    return cursor.fetchone() is not None

# Function to create a role if it does not exist
def create_role(cursor, role_name, role_password):
    if not role_exists(cursor, role_name):
        print(f"🔹 Creating role '{role_name}'...")
        cursor.execute(
            sql.SQL("CREATE ROLE {} WITH LOGIN PASSWORD %s CREATEDB;").format(sql.Identifier(role_name)),
            [role_password]
        )
    else:
        print(f"✅ Role '{role_name}' already exists.")

# Function to check if a database exists
def database_exists(cursor, db_name):
    cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s;"), [db_name])
    return cursor.fetchone() is not None

# Function to create a database if it does not exist
def create_database(cursor, db_name, owner):
    if not database_exists(cursor, db_name):
        print(f"🔹 Creating database '{db_name}'...")
        cursor.execute(
            sql.SQL("CREATE DATABASE {} OWNER {};").format(
                sql.Identifier(db_name), sql.Identifier(owner)
            )
        )
    else:
        print(f"✅ Database '{db_name}' already exists.")

# Main execution
def setup_database():
    print("🚀 Setting up PostgreSQL roles and database...")

    # Connect as admin user
    conn = connect_as_admin()
    cursor = conn.cursor()

    # Ensure the 'postgres' role exists
    create_role(cursor, "postgres", DB_ADMIN_PASSWORD)

    # Ensure the 'app_user' role exists
    create_role(cursor, DB_USER, DB_USER_PASSWORD)

    # Ensure the database exists
    create_database(cursor, DB_NAME, DB_USER)

    # Grant privileges to 'app_user'
    cursor.execute(
        sql.SQL("GRANT ALL PRIVILEGES ON DATABASE {} TO {};").format(
            sql.Identifier(DB_NAME), sql.Identifier(DB_USER)
        )
    )

    print("✅ Database setup completed successfully!")

    # Close connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    setup_database()
