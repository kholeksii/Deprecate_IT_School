import pytest
from src import my_func

@pytest.mark.parametrize("a, b, c", [(1, 2, 3), (4, 5, 9)])
def test_adding(a, b, c):
    assert my_func.add(a, b) == c

@pytest.mark.parametrize("a, b, c", [(3, 2, 1), (9, 5, 4)])
def test_sub(a, b, c):
    assert my_func.substraction(a, b) == c

@pytest.mark.parametrize("a, b, c", [(3, 2, 6), (1, 5, 5)])
def test_multy(a, b, c):
    assert my_func.mult(a, b) == c

@pytest.mark.parametrize("a, b, c", [(4, 2, 2), (10, 2, 5), (6, 2, 3)])
def test_div(a, b, c):
    assert my_func.division(a, b) == c

@pytest.mark.parametrize("a, b", [(4, 2), (16, 4)])
def test_sqr(a, b):
    assert my_func.square_root(a) == b