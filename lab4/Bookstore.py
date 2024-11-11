import uuid

from fastapi import FastAPI

app = FastAPI()

class Bookstore:

    def __init__(self) -> None:
        self.books = {}
        self.orders = {}

    def add_book(
        self,
        id: str,
        title: str,
        author: str,
        price: float,
        quantity: int,
    ):
        if (
            not isinstance(title, str)
            or not isinstance(author, str)
            or not (isinstance(price, float) or isinstance(price, int))
            or not isinstance(quantity, int)
            or not isinstance(id, str)
        ):
            raise TypeError

        if not id or not title or not author or price <= 0 or quantity < 1:
            raise ValueError

        if self.books.get(id):
            raise ValueError

        self.books[id] = {
            "title": title,
            "author": author,
            "price": price,
            "quantity": quantity,
        }

    def update_book(self, id: str, price: float, quantity: int):
        if not self.books.get(id):
            return "Error: no book with the specified id."
        if not (isinstance(price, float) or isinstance(price, int)) or not isinstance(
            quantity, int
        ):
            raise TypeError
        if price < 0 or quantity < 0:
            raise ValueError
        if price:
            self.books[id]["price"] = price
        if quantity:
            self.books[id]["quantity"] += quantity

    def get_book(self, id: str = None):
        if id:
            return self.books.get(id)
        list_books = []
        for id, info_book in self.books.items():
            book = info_book
            book["id"] = id
            list_books.append(book)
        return list_books

    def remove_book(self, id: str):
        if self.books.get(id):
            del self.books[id]

    def purchase_book(
        self,
        books_to_buy: list,
        name: str,
        phone: str,
    ) -> float:
        id = str(uuid.uuid4())
        total_order_cost = 0
        status = "Processing"

        for book in books_to_buy:
            if not self.books.get(book["id"]):
                return f"Error: there is no book with ID: '{book["id"]}'."

            book_in_bookstore = self.books[book["id"]]
            if book_in_bookstore["quantity"] < book["quantity"]:
                return -0.1
            book_in_bookstore["quantity"] -= book["quantity"]
            total_price = book_in_bookstore["price"] * book["quantity"]
            total_order_cost += total_price

        self.orders[id] = {
            "books": books_to_buy,
            "total_order_cost": total_order_cost,
            "status": status,
            "name": name,
            "phone": phone,
        }
        return total_order_cost

    def update_orderStatus(self, id: str, new_status: str):
        if not isinstance(new_status, str):
            raise TypeError
        if not self.orders.get(id):
            return "Error: there is no order with specified ID"
        self.orders[id]["status"] = new_status

    def get_order_byID(self, id: str):
        if not self.orders.get(id):
            return None
        return self.orders.get(id)

    def get_orders_byPhone(self, phone: str):
        list_orders = []
        for id, order in self.orders.items():
            if order["phone"] == phone:
                order["id"] = id
                list_orders.append(order)
        return list_orders

    ###
    ###

    def search_book(
        self,
        title: str,
    ) -> dict:
        return self.books.get(title)

    def find_book(self, title: str = None, author: str = None):
        list_books = []
        if title:
            book = self.search_book(title=title)
            if book:
                book["title"] = title
                list_books.append(book)
            return list_books
        if author:
            for title, info_book in self.books.items():
                if info_book["author"] == author:
                    book = info_book.copy()
                    book["title"] = title
                    list_books.append(book)
            return list_books
        return []

    def inventory_value(self) -> float:
        total_value = sum(
            book["price"] * book["quantity"] for book in self.books.values()
        )
        return total_value
