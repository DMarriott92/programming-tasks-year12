"""
Week 01 - Core Fundamentals
AQA A-Level Computer Science (7517) - Year 12

Tests for: task01_core_fundamentals.py

Expected functions in student file:
    - add(a, b)                         -> returns a + b
    - subtract(a, b)                    -> returns a - b
    - multiply(a, b)                    -> returns a * b
    - divide(a, b)                      -> returns a / b as float
    - int_to_str(n)                     -> returns string representation of n
    - str_to_int(s)                     -> returns integer from numeric string
    - is_even(n)                        -> returns True if n is even, False otherwise
    - modulo(a, b)                      -> returns a % b
    - calculate_average(values)         -> returns mean of a list of numbers as float

Run with:
    python -m pytest test_week01_core_fundamentals.py -v
"""

import pytest
from task01_core_fundamentals import (
    add,
    subtract,
    multiply,
    divide,
    int_to_str,
    str_to_int,
    is_even,
    modulo,
    calculate_average,
)


# ============================================================
# CORE TESTS — every student should pass these
# ============================================================

class TestAddition:
    def test_add_two_positive_integers(self):
        assert add(2, 3) == 5

    def test_add_positive_and_negative(self):
        assert add(-1, 5) == 4

    def test_add_two_zeros(self):
        assert add(0, 0) == 0


class TestSubtraction:
    def test_subtract_two_positives(self):
        assert subtract(10, 3) == 7

    def test_subtract_gives_negative_result(self):
        assert subtract(3, 10) == -7

    def test_subtract_zero(self):
        assert subtract(5, 0) == 5


class TestTypeConversion:
    def test_int_to_str_returns_string_type(self):
        result = int_to_str(42)
        assert isinstance(result, str)

    def test_int_to_str_correct_value(self):
        assert int_to_str(42) == "42"

    def test_str_to_int_returns_int_type(self):
        result = str_to_int("99")
        assert isinstance(result, int)

    def test_str_to_int_correct_value(self):
        assert str_to_int("99") == 99


class TestBooleanExpressions:
    def test_is_even_returns_true_for_even(self):
        assert is_even(4) is True

    def test_is_even_returns_false_for_odd(self):
        assert is_even(7) is False

    def test_is_even_zero_is_even(self):
        assert is_even(0) is True


# ============================================================
# EXPECTED TESTS — target grade students should pass these
# ============================================================

class TestMultiplication:
    def test_multiply_two_positives(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(99, 0) == 0

    def test_multiply_negative_numbers(self):
        assert multiply(-3, -4) == 12

    def test_multiply_positive_and_negative(self):
        assert multiply(3, -4) == -12


class TestDivision:
    def test_divide_returns_float(self):
        result = divide(10, 4)
        assert isinstance(result, float)

    def test_divide_exact_result(self):
        assert divide(10, 2) == 5.0

    def test_divide_produces_decimal(self):
        assert divide(10, 4) == 2.5


class TestModulo:
    def test_modulo_even_number_returns_zero(self):
        assert modulo(10, 2) == 0

    def test_modulo_odd_number_returns_one(self):
        assert modulo(11, 2) == 1

    def test_modulo_larger_divisor(self):
        assert modulo(5, 8) == 5


class TestCalculateAverage:
    def test_average_of_three_numbers(self):
        assert calculate_average([10, 20, 30]) == 20.0

    def test_average_single_value(self):
        assert calculate_average([5]) == 5.0

    def test_average_returns_float(self):
        result = calculate_average([1, 2])
        assert isinstance(result, float)

    def test_average_with_negatives(self):
        assert calculate_average([-10, 0, 10]) == 0.0


# ============================================================
# STRETCH TESTS — top-end students aiming for full marks
# ============================================================

class TestEdgeCasesAndErrors:
    def test_divide_by_zero_raises_error(self):
        """Dividing by zero should raise a ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

    def test_str_to_int_non_numeric_raises_error(self):
        """Passing a non-numeric string should raise a ValueError."""
        with pytest.raises(ValueError):
            str_to_int("hello")

    def test_calculate_average_empty_list_raises_error(self):
        """An empty list has no mean — should raise a ValueError."""
        with pytest.raises(ValueError):
            calculate_average([])

    def test_modulo_by_zero_raises_error(self):
        """Modulo by zero should raise a ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            modulo(5, 0)

    def test_add_floats_returns_correct_value(self):
        """Functions should handle float inputs gracefully."""
        assert add(1.5, 2.5) == pytest.approx(4.0)

    def test_divide_float_result_approx(self):
        """Use pytest.approx for floating point comparisons."""
        assert divide(1, 3) == pytest.approx(0.3333, rel=1e-3)
