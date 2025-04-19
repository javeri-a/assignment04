# # 
# Write a function that takes a list of numbers and returns the sum of those numbers.

# Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()


def sum_of_list(numbers):
    return sum(numbers)

def main():
    input_str = input("Enter a list of numbers separated by spaces: ")
    number_list = [float(num) for num in input_str.split()]
    
    total = sum_of_list(number_list)
    print(f"\nThe sum of the numbers is: {total}")

if __name__ == '__main__':
    main()
