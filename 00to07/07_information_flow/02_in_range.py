def in_range(n, low, high):
 
    if n >= low and n <= high:
        return True

    return False

def main():
  
    n = int(input("Enter a number: "))
    low = int(input("Enter the low range: "))
    high = int(input("Enter the high range: "))
    
    print(in_range(n, low, high))

if __name__ == '__main__':
    main()
