'''
Interface Segregation Principle (ISP)

Clients should not be forced to depend on interfaces they don’t use. Instead of one large interface, create multiple smaller, specific interfaces.
'''

# Defining multiple interfaces
class Switchable:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class AdjustableBrightness:
    def set_brightness(self, level):
        pass

class AdjustableTemperature:
    def set_temperature(self, temperature):
        pass

# Implementing only relevant interfaces
class Light(Switchable, AdjustableBrightness):
    def turn_on(self):
        print("Light turned on")

    def turn_off(self):
        print("Light turned off")

    def set_brightness(self, level):
        print(f"Light brightness set to {level}")

class Thermostat(Switchable, AdjustableTemperature):
    def turn_on(self):
        print("Thermostat turned on")

    def turn_off(self):
        print("Thermostat turned off")

    def set_temperature(self, temperature):
        print(f"Temperature set to {temperature} degrees")

# Usage
light = Light()
light.turn_on()
light.set_brightness(75)

thermostat = Thermostat()
thermostat.turn_on()
thermostat.set_temperature(22)

'''
Explanation: Each device class implements only the interfaces it needs, adhering to ISP.

Output:
Light turned on
Light brightness set to 75
Thermostat turned on
Temperature set to 22 degrees
'''