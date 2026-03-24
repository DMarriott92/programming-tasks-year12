import sqlite3

# Name of your database file
db_file = "school.db"

# Name of your SQL file
sql_file = "database_setup.sql"  # change this if your file has a different name

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Read SQL file
with open(sql_file, "r") as file:
    sql_script = file.read()

# Execute the SQL script
cursor.executescript(sql_script)

# Commit changes and close connection
conn.commit()
conn.close()

print(f"Database '{db_file}' created and populated using '{sql_file}'.")