def main():
    print("Let's add two numbers together!")
    first_input = input("Please enter the first number: ")
    first_number = int(first_input)
    second_input = input("Please enter the second number: ")
    second_number = int(second_input)
    total = first_number + second_number
    print("The sum of", first_number, "and", second_number, "is", total)
    
if __name__ == '__main__':
    main()

