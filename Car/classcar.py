# Define a Car class
class Car:
    # Initialize the Car object with year_model, make, and speed attributes
    def __init__(self, year_model, make):
        self.__year_model = year_model  # Assign year_model to the private attribute __year_model
        self.__make = make  # Assign make to the private attribute __make
        self.__speed = 0  # Initialize speed to 0

     # Getter method for __year_model attribute
    def get_year_model(self):
        return self.__year_model

    # Getter method for __make attribute
    def get_make(self):
        return self.__make

    # Getter method for __speed attribute
    def get_speed(self):
        return self.__speed

    # Setter method for __year_model attribute
    def set_year_model(self, year_model):
        self.__year_model = year_model

    # Setter method for __make attribute
    def set_make(self, make):
        self.__make = make

    # Method to increase the speed of the car by 5
    def accelerate(self):
        self.__speed += 5

    # Method to decrease the speed of the car by 5
    def brake(self):
        self.__speed -= 5
