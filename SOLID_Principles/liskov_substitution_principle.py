'''
Liskov Substitution Principle (LSP)

Subclasses should be substitutable for their base classes without breaking the program.
'''

class Vehicle:
    def start_engine(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Bicycle(Vehicle):
    def start_engine(self):
        raise Exception("Bicycles don't have engines")  # Violates LSP

# Refactoring to respect LSP
class NonEngineVehicle(Vehicle):
    def start_engine(self):
        pass  # Bicycles don’t need this method

# Usage
vehicles = [Car(), NonEngineVehicle()]

for vehicle in vehicles:
    if hasattr(vehicle, 'start_engine'):
        vehicle.start_engine()

'''
Explanation: In the refactored version, NonEngineVehicle can substitute Vehicle without throwing unexpected errors, following LSP.
Output:
Car engine started
If we add Bicycle() class inside vehicles list then we get the below error:
Traceback (most recent call last):
  File "/workspaces/python_coding/SOLID_Principles/liskov_substitution_principle.py", line 29, in <module>
    vehicle.start_engine()
  File "/workspaces/python_coding/SOLID_Principles/liskov_substitution_principle.py", line 17, in start_engine
    raise Exception("Bicycles don't have engines")  # Violates LSP
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Bicycles don't have engines
'''