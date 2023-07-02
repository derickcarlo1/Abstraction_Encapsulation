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
# Create an instance of the Fan class
# Demonstrate the usage of the Fan class methods