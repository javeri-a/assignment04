def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True

    return False

def main():
    # Example usage of the in_range function
    n = int(input("Enter a number: "))
    low = int(input("Enter the low range: "))
    high = int(input("Enter the high range: "))
    
    print(in_range(n, low, high))

if __name__ == '__main__':
    main()
