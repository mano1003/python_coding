'''
Separation of Concerns (SoC) is a fundamental design principle where different parts of a system are divided into distinct sections, 
each responsible for a specific functionality. This modularity improves maintainability, readability, and flexibility, 
making it easier to change or expand parts of the code without affecting others.

Real-World Example: E-commerce Web Application

Imagine we’re building a simple e-commerce application. We have several main responsibilities here:

	1.	Managing products (adding, listing, updating product information)
	2.	Processing orders (handling the purchase process, calculating totals)
	3.	Handling payments (charging the customer, validating payment info)
	4.	Managing user accounts (registration, authentication, user profiles)

Using SoC, we would structure this application by separating these concerns into different modules or layers. Here’s how it might look:

1. Product Service

This module is dedicated to managing everything related to products. It contains methods for adding, updating, and retrieving product data, 
keeping it isolated from order processing, payments, or user management.

'''
# Products Services Class - Having methods and attributes releted to product alone
class ProductService:
    # constructor
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_product(self, product_id):
        # Logic to retrieve product details
        pass

    def update_product(self, product_id, details):
        # Logic to update product information
        pass

'''
2. Order Service

This module focuses on processing orders. It interacts with the ProductService to get product information and processes customer orders.

'''

class OrderService:
    def __init__(self, product_service):
        self.product_service = product_service
        self.orders = []

    def create_order(self, product_id, quantity):
        product = self.product_service.get_product(product_id)
        # Calculate order total, create order, etc.
        order = {"product": product, "quantity": quantity, "status": "pending"}
        self.orders.append(order)
        return order
    
'''
3. Payment Service

The PaymentService module manages payment processing. It’s separate from order management and product data, so it can be changed independently.
'''

class PaymentService:
    def process_payment(self, order, payment_info):
        # Logic to charge the user
        print("Processing payment for order:", order)
        return "Payment Successful"

'''
4. User Service

This module handles user-related functions like registering new users, logging in, and updating user profiles.
'''

class UserService:
    def register_user(self, user_info):
        # Logic to register user
        pass

    def login(self, username, password):
        # Logic to authenticate user
        pass

'''
Tying It All Together with SoC

In the main application, these modules interact but don’t interfere with each other’s internal details. 
This structure allows each module to be developed, tested, and maintained independently.
'''

# Example main application code
product_service = ProductService()
order_service = OrderService(product_service)
payment_service = PaymentService()
user_service = UserService()

# Scenario: User places an order and makes payment
product_service.add_product({"id": 1, "name": "Laptop", "price": 1200})
order = order_service.create_order(product_id=1, quantity=2)
payment_service.process_payment(order, payment_info={"card_number": "1234-5678-9012-3456"})

'''
Benefits of SoC

	1.	Modularity: Each service (product, order, payment, user) has its own dedicated space, making the code cleaner and more organized.
	2.	Maintainability: Changes in one service (e.g., payment logic) don’t affect others, allowing for easier updates and bug fixes.
	3.	Scalability: New functionalities can be added (e.g., a new ShippingService) without major refactoring.
	4.	Testability: Individual modules can be tested independently, allowing for isolated unit testing.

By following SoC, we create a flexible, modular application that’s easier to work on, update, and scale—key advantages for long-term software projects.
'''