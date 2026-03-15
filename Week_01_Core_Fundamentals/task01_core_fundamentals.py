"""
Week 01 - Core Fundamentals
AQA A-Level Computer Science (7517) - Year 12

TODO: Implement each function below so that all tests pass.
Run the tests with:
    python -m pytest test_week01_core_fundamentals.py -v

Work through the tiers in order:
    CORE     — basic implementation, no error handling needed
    EXPECTED — think about edge cases and return types
    STRETCH  — add input validation and raise appropriate errors
"""


# ============================================================
# CORE
# ============================================================

def add(a, b):
    """Returns the sum of a and b."""
    pass


def subtract(a, b):
    """Returns a minus b."""
    pass


def multiply(a, b):
    """Returns a multiplied by b."""
    pass


def divide(a, b):
    """
    Returns a divided by b as a float.
    STRETCH: raise ZeroDivisionError if b is 0.
    """
    pass


def int_to_str(n):
    """Returns the string representation of integer n."""
    pass


def str_to_int(s):
    """
    Returns the integer value of numeric string s.
    STRETCH: raise ValueError if s cannot be converted.
    """
    pass


def is_even(n):
    """Returns True if n is even, False otherwise."""
    pass


def modulo(a, b):
    """
    Returns a % b.
    STRETCH: raise ZeroDivisionError if b is 0.
    """
    pass


# ============================================================
# EXPECTED
# ============================================================

def calculate_average(values):
    """
    Takes a list of numbers and returns the mean as a float.
    Do NOT use sum() or statistics.mean() — calculate it manually.
    STRETCH: raise ValueError if the list is empty.
    """
    pass


# ============================================================
# Run a quick manual demo when this file is executed directly
# ============================================================

if __name__ == "__main__":
    print("add(2, 3)        =", add(2, 3))
    print("subtract(10, 3)  =", subtract(10, 3))
    print("multiply(4, 5)   =", multiply(4, 5))
    print("divide(10, 4)    =", divide(10, 4))
    print("int_to_str(42)   =", int_to_str(42))
    print("str_to_int('99') =", str_to_int("99"))
    print("is_even(4)       =", is_even(4))
    print("modulo(11, 2)    =", modulo(11, 2))
    print("average([1,2,3]) =", calculate_average([1, 2, 3]))
