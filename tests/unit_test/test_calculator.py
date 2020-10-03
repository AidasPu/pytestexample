from function.calculator import Calculator
import pytest

@pytest.fixture()
def answer():
    return 4



def test_addition(answer):
    calculator = Calculator()
    assert calculator.add(2, 2) == answer

def test_addition_with_char_exception():
    calculator = Calculator()
    with pytest.raises(Exception):
        assert calculator.add("three", 2)

def test_substraction(answer):
    calculator = Calculator()
    assert calculator.substract(6, 2) == answer

def test_sbustraction_wrong_value():
    calculator = Calculator()
    with pytest.raises(Exception):
        assert calculator.substract("test", 2) == 0


def test_multiplication(answer):
    calculator = Calculator()
    assert calculator.multiply(2, 2) == answer

def test_division(answer):
    calculator = Calculator()
    assert calculator.divide(8, 2) == answer

def test_raise_by_power():
    calculator = Calculator()
    assert calculator.power(10, 2) == 100


"vsdvdssdvsdvsdvsdv"


