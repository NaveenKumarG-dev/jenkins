import pytest

from calculate import add, subtract, multiply, divide


def test_adds_numbers():
    assert add(2, 3) == 5


def test_subtracts_numbers():
    assert subtract(7, 3) == 4


def test_multiplies_numbers():
    assert multiply(4, 3) == 12


def test_divides_numbers():
    assert divide(10, 2) == 5


def test_divide_by_zero_raises_an_error():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)