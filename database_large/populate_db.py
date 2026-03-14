import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect("school_full.db")

# Open SQL file
with open("database_setup_full.sql", "r") as f:
    sql_script = f.read()

# Execute SQL script
conn.executescript(sql_script)

# Save changes
conn.commit()

print("Database created successfully!")

conn.close()