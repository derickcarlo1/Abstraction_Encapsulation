from classpet import Pet

if __name__ == "__main__":
    print("\033[1;35m" + "Welcome to Pet Info" + "\033[0m")  # Magenta color

    pet = Pet()

    name = input("Enter the name of your pet: ")
    pet.set_name(name)

    animal_type = input("Enter the type of animal your pet is: ")
    pet.set_animal_type(animal_type)

    age = input("Enter the age of your pet: ")
    pet.set_age(age)

    print("\n\033[1;36m*** Pet Information ***\033[0m")  # Cyan color
    print("\033[1;33mName:\033[0m", pet.get_name())  # Yellow color
    print("\033[1;33mAnimal Type:\033[0m", pet.get_animal_type())
    print("\033[1;33mAge:\033[0m", pet.get_age())