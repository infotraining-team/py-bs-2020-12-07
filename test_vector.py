import pytest
from vector import Vector

def test_creating_vector_with_coords():
    assert Vector(1, 1) != None

def test_check_vector_coords_not_using_attributes():
    vec = Vector(1, 2)
    with pytest.raises(AttributeError):
        vec.x == 1

def test_check_vector_coords():
    vec = Vector(1, 2)
    assert vec.get_x() == 1
    assert vec.get_y() == 2

def test_check_vector_length():
    vec = Vector(1, 1)
    assert vec.length() == pytest.approx(1.4142, 0.001)

def test_vector_position_change():
    vec = Vector(1, 1)
    vec.set_x(2)
    vec.set_y(2)
    assert vec.length() == pytest.approx(2.8284, 0.001)


    # import math
    # math.sqrt(x*x + y*y)
