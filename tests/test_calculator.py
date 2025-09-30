import pytest
from LabWork.src.calculator.calculator import Calculator


@pytest.mark.parametrize("string", ["7 * 9", "80   +      50"])
def test_remove_spaces_true(string: str):
    assert Calculator.remove_spaces(string)


@pytest.mark.parametrize("string", ["10+10", "1   * 4", "6 * * 6", "2.5*8.6",
                                    "(2*(10-5)**2-10*5)*(-1)", "0**(-10)"])
def test_is_input_string_correct_true(string: str):
    assert Calculator.is_input_string_correct(string)


@pytest.mark.parametrize("string", ["2(10-5)", "(2/8)3", "2*() - 10", "E404",
                                    "10..25 + 2", " 10 ? 5*5", "(10+(5-7)+3*(10/(5)) - 5*(30)",
                                    ")*5 - 8 ) + 10*(("])
def test_is_input_string_correct_false(string: str):
    assert not Calculator.is_input_string_correct(string)


@pytest.mark.parametrize("string", ["-2*10", "(-2)**2"])
def test_is_math_expression_correct_true(string: str):
    assert Calculator.is_math_expression_correct(string)


@pytest.mark.parametrize("string", ["80/9*", "/5*4", "90-5+"])
def test_is_math_expression_correct_false(string: str):
    assert not Calculator.is_math_expression_correct(string)


def test_parentheses_finder_true():
    assert Calculator.parentheses_finder("(2*(10+(-2)))-1") == "(-2)"
    assert Calculator.parentheses_finder("10**2-(8+6)+10*(4-3)") == "(8+6)"
    assert Calculator.parentheses_finder("2**((-6)*1+(50-(-7*10+(10+35))))") == "(-6)"


def test_parentheses_finder_false():
    assert not Calculator.parentheses_finder("(10-6)+(2**3)") == "(2**3)"
    assert not Calculator.parentheses_finder("4*((-5)*10+(80-76))") == "(80-76)"
    assert not Calculator.parentheses_finder("10*(8+6)") == "8+6"


"""
find_numbers finds numbers without sign.
Sign is handled in outer methods like summation
"""


def test_find_numbers_true():
    assert Calculator.find_numbers("25*90-148+90//5", 2, 1) == (
        (25.0, 2), (90.0, 2))
    assert Calculator.find_numbers("10+5+7**9", 6, 2) == (
        (7.0, 1), (9.0, 1))
    assert Calculator.find_numbers("8+90//-10", 4, 3) == (
        (90.0, 2), (10.0, 2))
    assert Calculator.find_numbers("8.25+10.75", 4, 1) == (
        (8.25, 4), (10.75, 5))
    assert Calculator.find_numbers("-0+1", 2, 1) == (
        (0.0, 1), (1.0, 1))
    assert Calculator.find_numbers("-100-80", 4, 1) == (
        (100.0, 3), (80.0, 2))


"""
Summation takes as the argument a string without parentheses.
"""


def test_summation_true():
    assert Calculator.summation("10+1*-2**2") == "14.0"
    assert Calculator.summation("-5+10") == "5.0"
    assert Calculator.summation("-2*-2**3+8-2**2") == "20.0"


def test_unary_operation_true():
    assert Calculator.unary_operation("-0.0") == "0.0"
