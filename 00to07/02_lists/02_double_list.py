# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

# Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':

def main():
    numbers: list[int] = [1, 2, 3, 4]
    for i in range(len(numbers)):
        elem_at_index = numbers[i]
        numbers[i] = elem_at_index * 2
    print(numbers)

if __name__ == '__main__':
    main()
