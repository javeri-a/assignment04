
def main():
    try:
        dividend = int(input("Please enter an integer to be divided: "))
        divisor = int(input("Please enter an integer to divide by: "))
        
        if divisor == 0:
            print("Cannot divide by zero.")
            return

        quotient = dividend // divisor
        remainder = dividend % divisor

        print(f"\nThe result of this division is {quotient} with a remainder of {remainder}")
    except ValueError:
        print("Please enter valid integers.")

if __name__ == '__main__':
    main()
