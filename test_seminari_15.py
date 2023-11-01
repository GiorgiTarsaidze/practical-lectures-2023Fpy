from seminari_15 import *

books = {}

# "Topuria": ["Math", "fsf"],
# "Franz Kafka": "Gardasaxva",

def test_view_books():
    add_book("Topuria", ["Math", "fsf"])
    add_book("Topurgdfgia", "fsf")
    # ar mushaobs

    assert view_books() == "[]"

def test_add_book():
    assert add_book("Topuria", ["Math", "fsf"]) == True

def test_remove_book():
    add_book("Topuria", ["Math", "fsf"])

    assert remove_book("Topuria") == True
    assert remove_book("Topuria") == False



def test_search_book():
    add_book("Topuria", ["Math", "fsf"])

    assert search_book("Math") == True

    remove_book("Topuria")

    assert search_book("Math") == False

test_view_books()
