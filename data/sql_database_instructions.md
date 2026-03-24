# Implementing the School Database in VS Code

This guide will show you how to set up and use the `school_full.db` or 'school.db' database for your AQA Year 12 Computer Science tasks using **VS Code**.

---

## 1. Check Your Tools

Make sure you have the following installed:

- **Python 3** (comes with `sqlite3` module)
- **VS Code** (latest version recommended)
- **SQLite** (optional; Python includes `sqlite3`, but the SQLite CLI is useful)

---

## 2. Download the Database Files

Clone this repository or create your own .sql file similar to the ones I've made.

## 3. Option A – Use the Pre-Built Database

1. Open VS Code and **open your repository folder**.
2. Make sure `school_full.db` is inside the `data/` folder.
3. Test the database using Python:
4. populate_db.py

```python
import sqlite3

# Connect to the database
conn = sqlite3.connect("data/school_full.db")
cursor = conn.cursor()

# Run a simple query
cursor.execute("SELECT * FROM Students;")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

## 3.1 Option B - Command lines

Open a terminal in VS Code.

**Navigate to the data/ folder:**

cd data

**Run the SQL script to create and populate the database:**

sqlite3 school_full.db < database_setup_full.sql

This will create school_full.db with all tables and example data.

**Check the tables:**

sqlite3 school_full.db
sqlite> .tables

**You should see:**

Students  Teachers  Courses  Classes  Enrolments

**Option C – Create the Database Using Python Script**

Make sure populate_db.py is in the data/ folder.

Run the script in VS Code terminal:

python data/populate_db.py

This creates school_full.db with all tables and data.

Verify by connecting in Python or using SQLite CLI.
