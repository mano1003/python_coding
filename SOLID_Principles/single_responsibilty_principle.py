'''
1. Single Responsibility Principle (SRP)

Each class should have only one reason to change, meaning it should be responsible for only one part of the functionality.

Example: Order Processing System
'''

# Class to manage order data
class Order:
    def __init__(self, items):
        self.items = items
        self.total = sum(item['price'] for item in items)

# Class to handle printing the invoice
class InvoicePrinter:
    def print_invoice(self, order):
        print("Invoice:")
        for item in order.items:
            print(f"{item['name']}: ${item['price']}")
        print(f"Total: ${order.total}")

# Class to handle payment processing
class PaymentProcessor:
    def process_payment(self, order, payment_details):
        print(f"Processing payment of ${order.total} with method {payment_details['method']}")

# Usage
order = Order([{"name": "Laptop", "price": 1200}, {"name": "Mouse", "price": 50}])
printer = InvoicePrinter()
payment_processor = PaymentProcessor()

printer.print_invoice(order)
payment_processor.process_payment(order, {"method": "Credit Card"})

'''
Explanation: Each class has a single responsibility:
	•	Order handles the order data.
	•	InvoicePrinter prints the invoice.
	•	PaymentProcessor handles payments.
'''