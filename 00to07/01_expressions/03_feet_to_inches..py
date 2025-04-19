# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

# Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
# Solution
# """
# An example program with constants
# """

# INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.

# def main():
#     feet: float = float(input("Enter number of feet: "))  # Get the number of feet, make sure to cast it to a float!
#     inches: float = feet * INCHES_IN_FOOT  # Perform the conversion
#     print("That is", inches, "inches!")
    
    
# # This provided line is required at the end of a Python file
# # to call the main() function.
# if __name__ == '__main__':
#     main()







def main():
    while True:
        try:
            feet_input = input("Enter length in feet (or type 'exit' to quit): ")
            if feet_input.lower() == 'exit':
                break
            feet = float(feet_input)
            inches = feet * 12
            print(f"\n{feet} feet is equal to {inches} inches.\n")
        except ValueError:
            print("Please enter a valid number for feet.\n")

if __name__ == '__main__':
    main()
