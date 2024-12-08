import pytest
import pytest_mastering.source.my_functions as my_functions


def test_add():
    result = my_functions.add(2,2)
    expected = 4
    assert result == expected

def test_add_strinf():
    result = my_functions.add("I like ", "testing my code !")
    expected = "I like testing my code !"
    assert result == expected

def test_divide():
    result = my_functions.divide(4, 2)
    expected = 2
    assert result == expected

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(4, 0)
   