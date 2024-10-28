'''
SOLID Principles - Dependency Injection
Definition:
Dependency Injection (DI) is about providing an object’s dependencies from the outside rather than letting the object create them itself. 
This principle helps to keep the code modular, flexible, and easier to test.

Here’s a real-world example using a notification service. 
Let’s say you have an application that can send notifications to users via email, SMS, or push notifications. 
Here’s how Dependency Injection can help us organize and manage these services.

Without Dependency Injection:

In a traditional approach, the NotificationSender class might decide within itself which notification service (Email, SMS, Push) to use, like this:

class EmailService:
    def send(self, message):
        print("Sending email:", message)

class SMSService:
    def send(self, message):
        print("Sending SMS:", message)

class NotificationSender:
    def __init__(self):
        # Directly creating instances of services, which makes testing difficult and limits flexibility
        self.email_service = EmailService()
        self.sms_service = SMSService()
    
    def notify(self, message, method):
        if method == 'email':
            self.email_service.send(message)
        elif method == 'sms':
            self.sms_service.send(message)

Issues with This Approach

	1.	Tight Coupling: NotificationSender is tightly coupled with the specific services (EmailService and SMSService). 
    If we want to add a new notification method (like Push), we’d need to modify the NotificationSender class.
	2.	Difficulty in Testing: To test NotificationSender, we can’t substitute these dependencies easily.
'''

class EmailService:
    def send(self, message):
        print("Sending email:", message)

class SMSService:
    def send(self, message):
        print("Sending SMS:", message)

class NotificationSender:
    def __init__(self, service):
        # Injecting the dependency through the constructor
        self.service = service
    
    def notify(self, message):
        # Now `NotificationSender` only calls the service, making it modular
        self.service.send(message)

# Example usage
email_service = EmailService()
sms_service = SMSService()

# Injecting the specific service we need
notification_sender = NotificationSender(email_service)
notification_sender.notify("Hello via Email!")

# We can easily switch to SMS by injecting a different service
notification_sender_sms = NotificationSender(sms_service)
notification_sender_sms.notify("Hello via SMS!")

'''
Benefits of Dependency Injection:

	1.	Loose Coupling: NotificationSender is no longer coupled to specific notification methods. It just uses a generic interface (send method), so you can easily add new services.
	2.	Flexibility: You can swap out services without modifying the NotificationSender class.
	3.	Easier Testing: To test NotificationSender, you could inject a mock or dummy service, which isolates the code under test and avoids side effects (like actually sending an email).
'''