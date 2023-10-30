
# import pytest

# def test_add():
#     assert add(2,3) == 5
#     assert add(6,3) == 9
#     assert add(1,-2) == -1
#     assert add(0,29) == 29
#     assert add(2,2) == 4

# def test_subtract():
#     assert subtract(2,3) == -1
#     assert subtract(2,0) == 2
#     assert subtract(18,2) == 16
#     assert subtract(123534252,2) == 123534250
#     assert subtract(-2,-3) == 1


# def test_multiply():
#     assert multiply(5,2) == 10
#     assert multiply(18,2) == 36

# def test_divide():
#     assert divide(10,2) == 5

# def test_zeroDivision():
#     with pytest.raises(ZeroDivisionError):
#         divide(16,0)
#         divide(6,0)
#         divide(0,0)


from seminari_14 import *

def test_count_vowels():
    assert count_vowel("banana") == 3
    assert count_vowel("text") == 1

def test_reverse_string():
    assert reverse_string("banana") == "ananab"
    assert reverse_string("text") == "txet"

def test_palindrome():
    assert palindrome("wow") == True
    assert palindrome("fksdfsdf") == False
