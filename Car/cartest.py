from classcar import Car
import pyfiglet

# Print program header
header = pyfiglet.figlet_format("Car Speed Test")
print(header)

# Create a Car object
car = Car(2022, "Example Make")

# Accelerate the car five times
print("Accelerating...")
for _ in range(5):
    car.accelerate()
    speed = car.get_speed()
    print(f"Current speed: {speed} mph")

# Brake the car five times
print("\nBraking...")
for _ in range(5):
    car.brake()
    speed = car.get_speed()
    print(f"Current speed: {speed} mph")

# Modify the car attributes using setters
car.set_year_model(2023)
car.set_make("New Make")

# Get the updated car attributes using getters
year_model = car.get_year_model()
make = car.get_make()

print(f"\nUpdated Car Details:")
print(f"Year Model: {year_model}")
print(f"Make: {make}")