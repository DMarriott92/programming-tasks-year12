## Week 18 — SQL Programming & Database Applications

```markdown
# Week 18 — SQL Programming & Database Applications

This week builds complete database-driven applications in Python — moving from
individual SQL queries to integrated programs that use parameterised queries,
aggregate functions, and user authentication backed by a database.

## Tasks

| File | Task | Key Concept |
|------|------|-------------|
| `01_parameterised_queries.py` | Use parameterised SQL queries to prevent SQL injection | Parameterised queries, security |
| `02_aggregate_sql_reports.py` | Generate reports using SQL aggregate functions | `COUNT`, `SUM`, `AVG`, `GROUP BY` |
| `03_database_login_system.py` | Build a login system that authenticates users against a database | SQL + Python integration, hashing passwords |

## Why Parameterised Queries?
Never build SQL queries by concatenating strings with user input:
```python
# DANGEROUS — vulnerable to SQL injection
query = "SELECT * FROM users WHERE name = '" + user_input + "'"

# SAFE — use parameterised queries
query = "SELECT * FROM users WHERE name = ?"
cursor.execute(query, (user_input,))
```

## AQA Spec Links
- SQL — aggregate functions, `GROUP BY`
- Database application programming
- Defensive programming and security
```