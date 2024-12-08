import pytest

import pytest_mastering.source.shapes as shapes

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

def test_area(my_rectangle):
    assert my_rectangle.area() == 200

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 60
