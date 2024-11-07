import pytest
from bookstore import Bookstore

def test_add_book():
    store = Bookstore()
    store.add_book("Book1", "Author1", 10.0, 5)
    assert store.search_book("Book1") == {"author": "Author1", "price": 10.0, "quantity": 5}

    store.add_book("Book1", "Author1", 10.0, 3)
    assert store.search_book("Book1")["quantity"] == 8

def test_remove_book():
    store = Bookstore()
    store.add_book("Book1", "Author1", 10.0, 5)
    store.remove_book("Book1")
    assert store.search_book("Book1") is None

    store.remove_book("NonExistentBook")

def test_search_book():
    store = Bookstore()
    store.add_book("Book1", "Author1", 10.0, 5)
    assert store.search_book("Book1") == {"author": "Author1", "price": 10.0, "quantity": 5}
    assert store.search_book("NonExistentBook") is None

def test_purchase_book():
    store = Bookstore()
    store.add_book("Book1", "Author1", 10.0, 5)
    total_price = store.purchase_book("Book1", 2)
    assert total_price == 20.0
    assert store.search_book("Book1")["quantity"] == 3

    with pytest.raises(ValueError):
        store.purchase_book("Book1", 10)

    with pytest.raises(ValueError):
        store.purchase_book("NonExistentBook", 1)

def test_inventory_value():
    store = Bookstore()
    store.add_book("Book1", "Author1", 10.0, 5)
    store.add_book("Book2", "Author2", 20.0, 3)
    assert store.inventory_value() == 110.0

def test_edge_cases():
    store = Bookstore()

    with pytest.raises(ValueError):
        store.add_book("Book1", "Author1", -10.0, 5)
    with pytest.raises(ValueError):
        store.add_book("Book1", "Author1", 10.0, -5)

    store.add_book("Book2", "Author2", 15.0, 0)
    with pytest.raises(ValueError):
        store.purchase_book("Book2", 1)

    store.remove_book("NonExistentBook")

    assert store.search_book("") is None
