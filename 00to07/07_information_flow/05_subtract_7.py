def main():
    num: int = int(input("Enter a number: "))  # Taking input from the user
    num = subtract_seven(num)  # Subtract 7 from the number
    print("This is the result after subtracting 7: ", num)

def subtract_seven(num):
    num = num - 7  # Subtract 7 from the input number
    return num

if __name__ == '__main__':
    main()
