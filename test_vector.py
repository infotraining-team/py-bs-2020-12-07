import pytest
from vector import Vector

## rewrite test to reflect properties for vector:
## v = Vector(1,2)
## v.x - property
## v.y - property
## v.length - read only length property

def test_creating_vector_with_coords():
    assert Vector(1, 1) != None

# def test_check_vector_coords_not_using_attributes():
#     vec = Vector(1, 2)
#     with pytest.raises(AttributeError):
#         vec.x == 1

def test_check_vector_coords():
    vec = Vector(1, 2)
    assert vec.x == 1
    assert vec.y == 2

def test_check_vector_length():
    vec = Vector(1, 1)
    assert vec.length() == pytest.approx(1.4142, 0.001)
    ## should optimize for math.sqrt called only once per coordinates changes

def test_vector_position_change():
    vec = Vector(1, 1)
    vec.length()
    vec.set_x(2)
    vec.set_y(2)
    assert vec.length() == pytest.approx(2.8284, 0.001)


    # import math
    # math.sqrt(x*x + y*y)
