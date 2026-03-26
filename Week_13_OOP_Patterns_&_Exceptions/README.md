## Week 13 — OOP Patterns & Exceptions

```markdown
# Week 13 — OOP Patterns & Exceptions

This week covers exception handling — making programs robust against unexpected
inputs — and introduces design patterns, which are reusable solutions to common
programming problems.

## Tasks

| File | Task | Key Concept |
|------|------|-------------|
| `01_strategy_pattern_demo.py` | Implement the Strategy design pattern to swap sorting algorithms at runtime | Design patterns, polymorphism |
| `02_exception_handling_framework.py` | Build a reusable exception handling framework with custom exception classes | `try/except`, custom exceptions |
| `03_dynamic_object_generator.py` | Dynamically create objects based on runtime input | OOP, `__class__`, factory pattern |

## Exception Handling Reminder
```python
try:
    # code that might fail
except ValueError as e:
    # handle the specific error
except Exception as e:
    # catch-all fallback
finally:
    # always runs
```

## AQA Spec Links
- Exception handling
- Object-oriented programming — advanced
- Robust and defensive programming
```