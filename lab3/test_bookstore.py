import pytest
from bookstore import Bookstore
from models import Book

@pytest.fixture
def bookstore():
    return Bookstore()

def test_add_book(bookstore):
    bookstore.add_book("Python 101", "John Doe", "1234567890", 29.99, 10)
    assert len(bookstore.inventory) == 1

def test_add_duplicate_isbn(bookstore):
    bookstore.add_book("Python 101", "John Doe", "1234567890", 29.99, 10)
    with pytest.raises(ValueError):
        bookstore.add_book("Python Advanced", "Jane Smith", "1234567890", 35.99, 5)

def test_purchase_book(bookstore):
    bookstore.add_book("Python 101", "John Doe", "1234567890", 29.99, 10)
    order = bookstore.purchase_book("1234567890", 2)
    assert order.total_cost == 59.98

def test_search_books(bookstore):
    bookstore.add_book("Python 101", "John Doe", "1234567890", 29.99, 10)
    bookstore.add_book("Python Advanced", "Jane Smith", "0987654321", 35.99, 5)
    results = bookstore.search_books(title="Python 101")
    assert len(results) == 1
    assert results[0]["title"] == "Python 101"

def test_track_order(bookstore):
    bookstore.add_book("Python 101", "John Doe", "1234567890", 29.99, 10)
    order = bookstore.purchase_book("1234567890", 2)
    status = bookstore.track_order(order.id)
    assert status.status == "Processing"
