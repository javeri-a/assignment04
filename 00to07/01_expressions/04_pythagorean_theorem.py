
import math

def main():
    try:
        ab = float(input("Enter the length of AB: "))
        ac = float(input("Enter the length of AC: "))
        bc = math.sqrt(ab ** 2 + ac ** 2)
        print(f"\nThe length of BC (the hypotenuse) is: {bc}")
    except ValueError:
        print("Please enter valid numeric values for the sides.")

if __name__ == '__main__':
    main()
