'''
Open/Closed Principle (OCP):

Classes should be open for extension but closed for modification. You can add new functionality by extending existing code, rather than modifying it.
Processing credit card payment of $100
Processing PayPal payment of $150
'''

# Abstract Payment Processor
class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

# Concrete classes for each payment method
class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# Usage
def make_payment(payment_processor, amount):
    payment_processor.process_payment(amount)

make_payment(CreditCardPayment(), 100)
make_payment(PayPalPayment(), 150)

'''
Explanation: New payment methods can be added as subclasses of PaymentProcessor without modifying existing code.

Output:
Processing credit card payment of $100
Processing PayPal payment of $150
'''
