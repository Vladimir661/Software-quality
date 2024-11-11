import Bookstore as b
import unittest


class TestBookstore(unittest.TestCase):

    def setUp(self):
        self.books = b.Bookstore()
        self.books.add_book("1", "Some book", "Max", 100, 1)
        self.books.add_book("2", "Max`s book 2", "Max", 150, 2)
        self.books.add_book("3", "Another book", "King", 20, 3)
        self.books.add_book("4", "Book 3", "Steven", 50, 1)

    def test_add_book(self):
        self.books.add_book("123", "Test book", "Mark", 250, 4)
        self.assertEqual(
            self.books.books["123"],
            {
                "title": "Test book",
                "author": "Mark",
                "price": 250,
                "quantity": 4,
            },
        )
        with self.assertRaises(ValueError):
            self.books.add_book("123", "Another book", "Max", 100, 2)


    def test_update_book(self):
        self.assertEqual(self.books.books["1"]["quantity"], 1)
        self.books.update_book("1", 300, 1)
        self.assertEqual(self.books.books["1"]["quantity"], 2)
        self.assertEqual(self.books.books["1"]["price"], 300)

        error = self.books.update_book("0", 300, 1)
        self.assertEqual(error, "Error: no book with the specified id.")


    def test_remove_book(self):
        self.books.remove_book("1")
        book = self.books.get_book("1")
        self.assertEqual(None, book)

        self.books.remove_book("1")


    def test_purchase_book(self):
        total_order_cost = self.books.purchase_book(
            [{"id": "1", "quantity": 1}, {"id": "2", "quantity": 2}],
            "Danylo",
            "0967568236",
        )
        self.assertEqual(total_order_cost, 400)
        self.assertEqual(self.books.books["1"]["quantity"], 0)

        error = self.books.purchase_book(
            [{"id": "1", "quantity": 2}],
            "Danylo",
            "0967568236",
        )
        self.assertEqual(error, -0.1)

    # Перевірити, що замовлення створюється з унікальним ідентифікатором.
    # Перевірити, що всі необхідні деталі (клієнт, книги, кількість) включені у замовлення.
    # Перевірити, що клієнт може переглянути всі свої попередні замовлення.
    def test_get_order_byID(self):
        total_order_cost = self.books.purchase_book(
            [{"id": "1", "quantity": 1}],
            "Danylo",
            "0967568236",
        )
        self.assertEqual(1, len(self.books.orders))

        order_id = self.books.get_orders_byPhone("0967568236")[0]
        self.assertEqual(
            self.books.get_order_byID(order_id["id"]),
            {
                "id": order_id["id"],
                "books": [{"id": "1", "quantity": 1}],
                "total_order_cost": total_order_cost,
                "status": "Processing",
                "name": "Danylo",
                "phone": "0967568236",
            },
        )

    # Перевірити, що статус замовлення може бути змінений (наприклад, з "оплачено" на "відправлено").
    def test_update_orderStatus(self):
        self.books.purchase_book(
            [{"id": "1", "quantity": 1}],
            "Danylo",
            "0967568236",
        )
        order_id = self.books.get_orders_byPhone("0967568236")[0]
        self.assertEqual(order_id["status"], "Processing")

        self.books.update_orderStatus(order_id["id"], "Sended")
        self.assertEqual(order_id["status"], "Sended")
