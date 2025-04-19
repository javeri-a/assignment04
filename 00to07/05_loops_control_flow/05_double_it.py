def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))

    # Loop until the current value is greater than or equal to 100
    while curr_value < 100:
        # Double the current value
        curr_value = curr_value * 2
        # Print the current value followed by a space
        print(curr_value, end=" ")

# This provided line is required at the end
# of the Python file to call the main() function.
if __name__ == '__main__':
    main()
