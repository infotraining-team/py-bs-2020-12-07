import pytest
from vector import Vector

## rewrite test to reflect properties for vector:
## v = Vector(1,2)
## v.x - property
## v.y - property
## v.length - read only length property
## ***  bonus:
## v.pos = (1, 2)
## print(v.pos) -> (1, 2) (tuple)
## ***  bonus 2:
## 2D and 3D
## v.pos = (1, 2, 3)
## __init__(self, *args) - any number of arguments

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
    assert vec.length == pytest.approx(1.4142, 0.001)
    ## should optimize for math.sqrt called only once per coordinates changes

def test_length_is_readonly():
    vec = Vector(1, 1)
    with pytest.raises(AttributeError):
        vec.length = 123

def test_vector_position_change():
    vec = Vector(1, 1)
    vec.length
    vec.x = 2
    vec.y = 2
    assert vec.length == pytest.approx(2.8284, 0.001)

def test_adding_vectors():
    v1 = Vector(2, 3)
    v2 = Vector(3, 4)
    v3 = v1 + v2    
    assert v3.x == 5
    assert v3.y == 7
    assert v3.length == pytest.approx(8.602, 0.001)

def test_adding_in_place_vectors():
    v1 = Vector(2, 3)
    v2 = Vector(3, 4)
    v1 += v2    
    assert v1.x == 5
    assert v1.y == 7
    assert v1.length == pytest.approx(8.602, 0.001)

def test_geting_item():
    vec = Vector(2, 3)
    assert vec[0] == 2
    assert vec[1] == 3
    with pytest.raises(IndexError):
        vec[3] == None

def test_seting_item():
    vec = Vector(1, 1)
    vec[0] = 2
    vec[1] = 3
    with pytest.raises(IndexError):
        vec[3] == None

    # import math
    # math.sqrt(x*x + y*y)
