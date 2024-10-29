'''
Dependency Inversion Principle (DIP)

High-level modules should not depend on low-level modules. Both should depend on abstractions (interfaces).
'''

from abc import ABC, abstractmethod

# Abstract notification service
class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Concrete implementations
class EmailService(NotificationService):
    def send(self, message):
        print(f"Sending email: {message}")

class SMSService(NotificationService):
    def send(self, message):
        print(f"Sending SMS: {message}")

# High-level class depends on abstraction
class NotificationManager:
    def __init__(self, service: NotificationService):
        self.service = service

    def notify(self, message):
        self.service.send(message)

# Usage
email_service = EmailService()
sms_service = SMSService()

email_manager = NotificationManager(email_service)
sms_manager = NotificationManager(sms_service)

email_manager.notify("Hello via Email!")
sms_manager.notify("Hello via SMS!")

'''
	Explanation: NotificationManager depends on the NotificationService abstraction, not on specific implementations like EmailService or SMSService. 
    This allows flexibility to use any service without modifying NotificationManager.
Output:
Sending email: Hello via Email!
Sending SMS: Hello via SMS!
'''