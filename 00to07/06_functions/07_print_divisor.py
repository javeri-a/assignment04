def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):  # Start from 1 and go up to num (inclusive)
        if num % i == 0:  # If num is divisible by i with no remainder
            print(i)

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

if __name__ == '__main__':
    main()
