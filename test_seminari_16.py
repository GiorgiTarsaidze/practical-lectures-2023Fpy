from seminari_16 import *

def test_function():
    assert add_user("Giorgi", 28, "giorgi@example.com") == True

def test_find_user():
    assert find_user("Giorgi") == {'age': 28, 'email': 'giorgi@example.com'}


    assert add_user("Giorgi", 28, "giorgi@example.com") == False

    assert update_user("Alice", age=31)  == True

    assert update_user("Lasha", age=31)  == False

    assert delete_user("Giorgi") == True
    assert delete_user("Giorgi") == False

    assert find_user("Giorgi") == False
