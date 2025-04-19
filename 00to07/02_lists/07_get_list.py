def main():
    lst = []  # Initialize an empty list to store values

    val = input("Enter a value: ")  # Prompt the user to enter a value
    while val:  # Keep looping until the user presses Enter without typing anything
        lst.append(val)  # Add the entered value to the list
        val = input("Enter a value: ")  # Prompt the user for the next value

    print("Here's the list:", lst)  # Print the final list once the loop ends


if __name__ == '__main__':
    main()
