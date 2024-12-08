import pytest
import pytest_mastering.source.shapes as shapes


@pytest.mark.parametrize("side_length, expected_area", 
                         [(5, 25), 
                          (4, 16), 
                          (9, 81)])
def test_multiples_square_area(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area