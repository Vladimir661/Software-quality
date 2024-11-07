class Book:
    def __init__(self, title, author, isbn, price, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.quantity = quantity

class Order:
    def __init__(self, book, quantity):
        self.book = book
        self.quantity = quantity
        self.status = "Processing"
        self.id = id(self)

    def total_price(self):
        return self.book.price * self.quantity
