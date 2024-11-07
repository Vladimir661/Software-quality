class Bookstore:
    def __init__(self):
        self.inventory = {}
        self.orders = []

    def add_book(self, title, author, isbn, price, quantity):
        if isbn in self.inventory:
            raise ValueError("Книга з таким ISBN вже існує в інвентарі.")
        self.inventory[isbn] = {
            "title": title,
            "author": author,
            "price": price,
            "quantity": quantity
        }

    def purchase_book(self, isbn, quantity):
        if isbn not in self.inventory:
            raise ValueError("Книга з таким ISBN не знайдена.")
        book = self.inventory[isbn]
        if book["quantity"] < quantity:
            raise ValueError("Недостатньо примірників книги для покупки.")
        book["quantity"] -= quantity
        order = Order(isbn, quantity, book["price"] * quantity)
        self.orders.append(order)
        return order

    def track_order(self, order_id):
        for order in self.orders:
            if order.id == order_id:
                return order
        return None

    def search_books(self, title=None, author=None, isbn=None):
        results = []
        for book in self.inventory.values():
            if (title and title.lower() in book["title"].lower()) or \
               (author and author.lower() in book["author"].lower()) or \
               (isbn and isbn == book["isbn"]):
                results.append(book)
        return results

class Order:
    order_counter = 1

    def __init__(self, isbn, quantity, total_cost):
        self.id = Order.order_counter
        Order.order_counter += 1
        self.isbn = isbn
        self.quantity = quantity
        self.total_cost = total_cost
        self.status = "Processing"

    def update_status(self, status):
        self.status = status

    def __repr__(self):
        return f"Order(id={self.id}, isbn={self.isbn}, quantity={self.quantity}, total_cost={self.total_cost}, status={self.status})"
