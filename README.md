# Year 12 Programming Tasks
### AQA A-Level Computer Science (7517)

> Refer to the homework calendar on Google Classroom for weekly deadlines.

---

## Getting Started

Follow these steps **once** when you first set up the repo on your laptop.

### 1. Fork the Repo
Click the **Fork** button at the top-right of this page. This creates your own personal copy of the repo under your GitHub account — this is where all your work will live.

### 2. Clone Your Fork to Your Laptop
Open VS Code, press `Ctrl+Shift+P` and type **Git: Clone**. Paste the URL of **your fork** (not the teacher's original).

### 3. Install Python & Git
If you haven't already:
- [Download Python](https://www.python.org/downloads/) — install the latest version, and tick **"Add Python to PATH"** during setup
- [Download Git](https://git-scm.com/downloads/)

### 4. Install Dependencies
Open the terminal in VS Code (`Ctrl+` `` ` ``) and run:

```bash
pip install -r requirements.txt
```

### 5. Verify Everything Works
```bash
pytest
```
You should see pytest run and report that it collected tests. Don't worry if many fail at this point — that's expected before you've written any code.

---

## Weekly Tasks

Each week has its own folder. Open the folder for the current week to find your task files and test file.

| Week | Topic |
|------|-------|
| 01 | Core Fundamentals |
| 02 | GCSE Basics |
| 03 | Arrays, Lists & CSV Basics |
| 04 | Algorithms Intro |
| 05 | File Handling & Text Processing |
| 06 | Multi-Dimensional Structures, Dictionaries & Menus |
| 07 | OOP Fundamentals |
| 08 | File Handling & SQL Concepts |
| 09 | Modular Programming & Simple SQL CRUD |
| 10 | Sorting Algorithms Intro & Graphs |
| 11 | Decomposition & Problem Solving |
| 12 | Advanced OOP — Inheritance & Polymorphism |
| 13 | OOP Patterns & Exceptions |
| 14 | Data Structures — Linked Lists, Stacks, Queues & Hashing |
| 15 | Trees & Graph Traversal |
| 16 | Recursion & Efficient Algorithms |
| 17 | Relational Databases, DDL & SQL Joins |
| 18 | SQL Programming & Database Applications |
| 19 | Client-Server Programming & Web APIs |
| 20–22 | Integration Project |
| 23–26 | Final Major Project |

---

## Testing Your Work

Testing is a core part of how you will submit work. Each week folder contains a test file (`test_weekXX.py`) with tests already written for you to complete and run.

### Before Running Tests — Rename Your Files
Task files are prefixed with a number to indicate order (e.g. `1_average_calculator.py`). **pytest will not pick up files that start with a number**, so you must rename them before running tests — remove the number prefix:

```
1_average_calculator.py  →  average_calculator.py
```

### Running Tests
To run the tests for a specific week:

```bash
python -m pytest Week_01_Core_Fundamentals/test_week01.py -v
```

To run all tests across the entire repo:

```bash
pytest
```

### Understanding the Test File
Each test file has a short tutorial section at the top — read it before you start. Tests are split into three tiers:

- **Core** — must complete
- **Expected** — aim for these
- **Stretch** — optional challenge

Your job is to fill in the `# TODO` sections in the test file *before* writing your functions. This is called test-driven development, and it's standard practice in the industry.

A full interactive guide to writing and running your tests is available in the repo as `pytest_tutorial.html` — open it in your browser.

---

## Submitting Your Work

Commit and push your work to **your fork** at the end of each week.

```bash
git add .
git commit -m "Week 01 complete"
git push
```

Your teacher will review your fork directly, so make sure your latest work is pushed before the deadline. They will be checking both your test files and your implementations.

---

## Topics Covered

- Variables and data types
- Selection and iteration
- Lists, arrays and dictionaries
- Functions and modular programming
- File handling
- Object-oriented programming
- Algorithms — searching, sorting, recursion
- Data structures — linked lists, stacks, queues, trees, graphs
- Relational databases and SQL
- Client-server programming and web APIs