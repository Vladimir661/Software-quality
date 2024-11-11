import Bookstore as b
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
bookstore = b.Bookstore()


class Book(BaseModel):
    id: str
    title: str
    author: str
    price: float
    quantity: int


class BookUpdate(BaseModel):
    price: float
    quantity: int


class Order(BaseModel):
    books_to_buy: list
    name: str
    phone: str


class OrderStatusUpdate(BaseModel):
    new_status: str


@app.post("/books/")
def add_book(book: Book):
    return bookstore.add_book(
        book.id, book.title, book.author, book.price, book.quantity
    )


@app.put("/books/{book_id}")
def update_book(book_id: str, book_update: BookUpdate):
    return bookstore.update_book(book_id, book_update.price, book_update.quantity)


@app.get("/books/{book_id}")
def get_book(book_id: str = None):
    return bookstore.get_book(book_id)


@app.delete("/books/{book_id}")
def delete_book(book_id: str):
    return bookstore.remove_book(book_id)


@app.post("/orders/")
def add_order(order: Order):
    return bookstore.purchase_book(order.books_to_buy, order.name, order.phone)


@app.put("/orders/{order_id}/status")
def update_order_status(order_id: str, status_update: OrderStatusUpdate):
    return bookstore.update_orderStatus(order_id, status_update.new_status)


@app.get("/orders/{order_id}")
def get_order(order_id: str):
    return bookstore.get_order_byID(order_id)


@app.get("/customers/{phone}/orders")
def get_customer_orders(phone: str):
    return bookstore.get_orders_byPhone(phone)
