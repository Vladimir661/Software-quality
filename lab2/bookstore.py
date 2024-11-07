class Bookstore:
    def __init__(self):
        self.inventory = {}

    def add_book(self, title: str, author: str, price: float, quantity: int):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative.")
        if title in self.inventory:
            self.inventory[title]["quantity"] += quantity
        else:
            self.inventory[title] = {"author": author, "price": price, "quantity": quantity}

    def remove_book(self, title: str):
        if title in self.inventory:
            del self.inventory[title]
        else:
            print("Book not found in inventory.")

    def search_book(self, title: str) -> dict:
        return self.inventory.get(title, None)

    def purchase_book(self, title: str, quantity: int) -> float:
        if title not in self.inventory:
            raise ValueError("Book not found in inventory.")
        if quantity > self.inventory[title]["quantity"]:
            raise ValueError("Requested quantity exceeds available stock.")
        self.inventory[title]["quantity"] -= quantity
        return self.inventory[title]["price"] * quantity

    def inventory_value(self) -> float:
        return sum(item["price"] * item["quantity"] for item in self.inventory.values())
