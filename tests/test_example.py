import pytest
from exampleDir.exampleFile import special_math, greeting


def test_special_math_1():
    assert special_math(5, 4) == 9


def test_special_math_2():
    assert special_math(-5, -4) == 9


def test_special_math_3():
    assert special_math(-2, 4) == 6


def test_greeting_1():
    assert greeting("John") == "Hello John"


def test_greeting_2():
    with pytest.raises(TypeError):
        greeting(21)
