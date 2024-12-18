import pytest
import pytest_mastering.source.my_functions as my_functions
import time


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
   
@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(4, 2)
    assert result == 2

@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert my_functions.add(1, 2) == 3
    

@pytest.mark.xfail(reason="We know we can't divide by zero")
def test_divide_zero_broken():
    my_functions.divide(1, 0)

