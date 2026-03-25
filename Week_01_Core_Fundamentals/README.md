## Week 01 — Core Fundamentals

```markdown
# Week 01 — Core Fundamentals

This week focuses on the building blocks of Python programming. All six tasks require
you to implement functions **from scratch** without using Python's built-in shortcuts
— the goal is to understand what's happening under the hood.

## Tasks

| File | Task | Key Concept |
|------|------|-------------|
| `01_average_calculator.py` | Calculate the mean of a list | Loops, accumulation |
| `02_min_max_finder.py` | Find the minimum and maximum of a list | Comparison logic |
| `03_array_reversal.py` | Reverse a list without using `reverse()` or `[::-1]` | Index manipulation |
| `04_linear_search.py` | Search a list and return the index of a target value | Linear search algorithm |
| `05_string_parser.py` | Count words and detect palindromes | String manipulation |
| `06_temperature_converter.py` | Convert between Celsius and Fahrenheit | Arithmetic, functions |

## Restrictions
These tasks have deliberate restrictions to build understanding:
- `average_calculator` — must NOT use `sum()` or `statistics.mean()`
- `min_max_finder` — must NOT use Python's built-in `min()` or `max()`
- `array_reversal` — must NOT use `reverse()` or `[::-1]`

## Testing
A test file is provided: `test_week01.py`

Before running tests, rename your task files to remove the number prefix:
```
01_average_calculator.py  →  average_calculator.py
```

Then run:
```bash
python -m pytest test_week01.py -v
```

## AQA Spec Links
- Programming concepts — variables, sequence, selection, iteration
- Subroutines and functions
- String handling
```

---

---