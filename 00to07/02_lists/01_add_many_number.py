

def sum_of_list(numbers):
    return sum(numbers)

def main():
    input_str = input("Enter a list of numbers separated by spaces: ")
    number_list = [float(num) for num in input_str.split()]
    
    total = sum_of_list(number_list)
    print(f"\nThe sum of the numbers is: {total}")

if __name__ == '__main__':
    main()
