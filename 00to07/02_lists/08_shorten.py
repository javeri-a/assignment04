MAX_LENGTH: int = 3  # Define the maximum length for the list

def shorten(lst):
    # Keep removing elements from the end of the list until it's MAX_LENGTH items long
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()  # Remove and return the last element
        print(last_elem)  # Print the removed element

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()  # Get the list from the user
    shorten(lst)  # Shorten the list to the specified length

if __name__ == '__main__':
    main()
