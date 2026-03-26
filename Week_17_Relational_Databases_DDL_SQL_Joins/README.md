## Week 17 — Relational Databases, DDL & SQL Joins

```markdown
# Week 17 — Relational Databases, DDL & SQL Joins

This week moves into relational database design — multiple tables linked by
foreign keys — and introduces DDL (Data Definition Language) commands alongside
SQL joins. This directly maps to the AQA A-Level theory paper content on databases.

## Tasks

| File | Task | Key Concept |
|------|------|-------------|
| `01_database_practice.py` | Practice creating and querying a single-table database | SQL revision |
| `02_realational_database.py` | Design and create a multi-table relational database with foreign keys | Relational databases, foreign keys |
| `03_crosstable_queries.py` | Write SQL queries that join multiple tables | `JOIN`, cross-table queries |
| `04_automated_DDL.py` | Automate database creation using DDL commands from Python | DDL — `CREATE`, `DROP`, `ALTER` |

## Key SQL This Week
```sql
-- Inner join
SELECT students.name, grades.score
FROM students
INNER JOIN grades ON students.id = grades.student_id;

-- DDL
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
```

## AQA Spec Links
- Relational databases — tables, primary keys, foreign keys
- SQL DDL — `CREATE TABLE`, `DROP TABLE`
- SQL DML — `SELECT`, `JOIN`, `WHERE`
- Normalisation
```