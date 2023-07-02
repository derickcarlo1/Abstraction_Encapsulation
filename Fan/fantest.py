from classfan import Fan

def main():
    # Create two instances of the Fan class
    fan1 = Fan(Fan.FAST, 10, 'yellow', True)
    fan2 = Fan(Fan.MEDIUM, 5, 'blue', False)

    # Print details of Fan 1
    print("\033[1;34mFan 1:\033[0m")  # Blue color and bold style for fan label

    # Print attributes of Fan 1
    print("\033[1mSpeed:\033[0m", fan1.get_speed())  # Bold style for attribute name
    print("\033[1mRadius:\033[0m", fan1.get_radius())
    print("\033[1mColor:\033[0m", fan1.get_color())
    print("\033[1mOn:\033[0m", fan1.is_on())

    print("\n\033[1;34mFan 2:\033[0m")  # Blue color and bold style for fan label

    # Print attributes of Fan 2
    print("\033[1mSpeed:\033[0m", fan2.get_speed())
    print("\033[1mRadius:\033[0m", fan2.get_radius())
    print("\033[1mColor:\033[0m", fan2.get_color())
    print("\033[1mOn:\033[0m", fan2.is_on())
    
if __name__ == '__main__':
    main()
