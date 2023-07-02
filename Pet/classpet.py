import pyfiglet

# Setter & getter
class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age
    
if __name__ == "__main__":
    # Display welcome message with colored ASCII art
    ascii_banner = pyfiglet.figlet_format("Welcome to Pet Info")
    print("\033[1;35m" + ascii_banner + "\033[0m")  # Magenta color

    pet = Pet()

    # Get pet information from the user
    name = input("Enter the name of your pet: ")
    pet.set_name(name)

    animal_type = input("Enter the type of animal your pet is: ")
    pet.set_animal_type(animal_type)   

    age = input("Enter the age of your pet: ")
    pet.set_age(age)

    # Display pet information with colored output
    print("\n\033[1;36m*** Pet Information ***\033[0m")  # Cyan color
    print("\033[1;33mName:\033[0m", pet.get_name())  # Yellow color
    print("\033[1;33mAnimal Type:\033[0m", pet.get_animal_type())
    print("\033[1;33mAge:\033[0m", pet.get_age())