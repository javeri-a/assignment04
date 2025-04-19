# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

# What's your favorite animal? cow

# My favorite animal is also cow!


def main():
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    RESET = '\033[0m'

    animal = input("What's your favorite animal? ")
    print(f"\nMy favorite animal is also {BOLD}{ITALIC}{animal}{RESET}!")
    
if __name__ == '__main__':
    main()



def main():
    animals=input("whats your favorite animal?")
    print(f"/n my fvt animal is also {animals}")
    if __name__ == '__main__';
    main()