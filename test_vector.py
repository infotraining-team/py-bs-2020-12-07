import pytest
from vector import Vector

def test_creating_vector_with_coords():
    assert Vector(1, 1) != None

def test_check_vector_coords():
    vec = Vector(1, 2)
    assert vec.x == 1
    assert vec.y == 2

def test_check_vector_length():
    vec = Vector(1, 1)
    assert vec.length() == pytest.approx(1.4142, 0.001)

    # import math
    # math.sqrt(x*x + y*y)
