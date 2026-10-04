import pytest
from hypothesis import given, strategies as st

from calculator import add, multiply, divide


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(4, 5) == 20


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


@given(st.integers(), st.integers())
def test_add_property(a, b):
    assert add(a, b) == a + b