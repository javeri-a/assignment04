def main():
    for i in range(10, 20):  # Loop from 10 to 19
        if is_odd(i):
            print(f"{i} odd")
        else:
            print(f"{i} even")

def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns True.
    """
    return value % 2 == 1  # Returns True if odd, False if even

if __name__ == '__main__':
    main()
