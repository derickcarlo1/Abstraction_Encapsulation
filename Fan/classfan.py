import pyfiglet

# Define the Fan class
class Fan:
    # Constants for fan speeds
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5, color='blue', on=False):
        # Initialize fan attributes
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    def get_speed(self):
        # Get the speed of the fan
        return self.__speed

    def set_speed(self, speed):
        # Set the speed of the fan
        self.__speed = speed

    def is_on(self):
        # Check if the fan is on or off
        return self.__on

    def set_on(self, on):
        # Turn the fan on or off
        self.__on = on

    def get_radius(self):
        # Get the radius of the fan
        return self.__radius

    def set_radius(self, radius):
        # Set the radius of the fan
        self.__radius = radius

    def get_color(self):
        # Get the color of the fan
        return self.__color

    def set_color(self, color):
        # Set the color of the fan
        self.__color = color

# Print program header using pyfiglet and ANSI escape sequences for color
header = pyfiglet.figlet_format("Fan Program")
print("\033[1;34m" + header + "\033[0m")  # Blue color for header

# Create an instance of the Fan class
fan = Fan()

# Demonstrate the usage of the Fan class methods
print("\n\033[1;33mDemonstrating Fan Class Methods:\033[0m")  # Yellow color and bold style for section header

print("\033[1mFan Speed:\033[0m", fan.get_speed())  # Bold style for attribute name
fan.set_speed(Fan.FAST)
print("\033[1mFan Speed:\033[0m", fan.get_speed())

print("\033[1mFan Status:\033[0m", fan.is_on())
fan.set_on(True)
print("\033[1mFan Status:\033[0m", fan.is_on())

print("\033[1mFan Radius:\033[0m", fan.get_radius())
fan.set_radius(8)
print("\033[1mFan Radius:\033[0m", fan.get_radius())

print("\033[1mFan Color:\033[0m", fan.get_color())
fan.set_color("red")
print("\033[1mFan Color:\033[0m", fan.get_color())