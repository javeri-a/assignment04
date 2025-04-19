MINIMUM_HEIGHT : int = 50  

def tall_enough_extension():
    while True:
        height_input = input("How tall are you? ")
        if height_input == "":
            break
        height = float(height_input)
        
        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

def main():
    tall_enough_extension()


if __name__ == '__main__':
    main()
