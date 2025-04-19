def get_name():
    name = input("What's your name? ")
    return name  # Returns the name the user types in

def main():
    name = get_name()
    print("Hello", name, "! ❣")

if __name__ == '__main__':
    main()
