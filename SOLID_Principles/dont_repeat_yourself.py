'''
The DRY (Don’t Repeat Yourself) principle aims to reduce redundancy in code by ensuring that each piece of functionality is defined in one place. 
This reduces errors, improves maintainability, and makes code easier to update since changes only need to happen in one spot.

Real-World Example: User Authentication in a Web Application

Imagine we’re developing a web application where we need to:

	1.	Check if a user is authenticated.
	2.	Check if a user has admin privileges.
	3.	Validate user data before saving it to the database.

Without DRY, it’s easy to end up duplicating similar code across different parts of the application. Let’s look at how to avoid that using DRY principles.

Without DRY: Duplicated Code

Here’s what it might look like if we don’t follow DRY principles:
'''

# Checking if a user is authenticated
def access_dashboard(user):
    if user.is_authenticated:
        # Logic for accessing the dashboard
        print("Accessing dashboard")
    else:
        print("Please log in")

def access_admin_panel(user):
    if user.is_authenticated:
        if user.is_admin:
            # Logic for accessing the admin panel
            print("Accessing admin panel")
        else:
            print("Admin privileges required")
    else:
        print("Please log in")

# Checking if user data is valid
def register_user(user_data):
    if "username" in user_data and "password" in user_data:
        # Logic for registering the user
        print("User registered")
    else:
        print("Invalid user data")

'''
Issues with This Approach

	1.	Redundant Authentication Checks: The user.is_authenticated check is repeated in multiple places.
	2.	Repetitive Validation Logic: The data validation ("username" in user_data and "password" in user_data) might also be used in other parts of the application, leading to redundancy.
	3.	Difficult to Maintain: If the authentication or validation logic changes, we’d have to update it in multiple places, increasing the risk of bugs.

With DRY: Centralized, Reusable Functions

To apply DRY principles, we can refactor the code to centralize repeated logic into separate, reusable functions:
'''

# DRY solution: Centralized functions for common logic

def is_authenticated(user):
    return user.is_authenticated

def is_admin(user):
    return user.is_authenticated and user.is_admin

def validate_user_data(user_data):
    return "username" in user_data and "password" in user_data

# Now we use these reusable functions in our main code

def access_dashboard(user):
    if is_authenticated(user):
        print("Accessing dashboard")
    else:
        print("Please log in")

def access_admin_panel(user):
    if is_authenticated(user):
        if is_admin(user):
            print("Accessing admin panel")
        else:
            print("Admin privileges required")
    else:
        print("Please log in")

def register_user(user_data):
    if validate_user_data(user_data):
        print("User registered")
    else:
        print("Invalid user data")

'''
Benefits of This DRY Approach

	1.	Centralized Logic: Authentication and validation checks are now in reusable functions (is_authenticated, is_admin, validate_user_data), 
    so any updates to these checks need to happen in one place only.
	2.	Improved Readability: The main functions (access_dashboard, access_admin_panel, register_user) are now simpler and more readable.
	3.	Reduced Maintenance Overhead: Updating authentication or validation logic only requires changes to the centralized functions, 
    reducing the risk of inconsistencies and bugs.

Extending DRY to More Complex Applications

As applications grow, DRY principles can be applied even more broadly:

	•	Database Models: For instance, a BaseModel class can handle common database fields and methods, which other models inherit.
	•	API Responses: A single function for formatting API responses can reduce repetitive code across endpoints.
	•	Reusable Components: In frontend development, reusable UI components (buttons, forms, etc.) help to avoid redundant markup and styling.

In short, DRY principles make code more modular, consistent, and easier to maintain. By centralizing functionality, 
you avoid the pitfalls of redundancy and make the application more adaptable to change.
'''