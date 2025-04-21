def main():
    num: int = int(input("Enter a number: ")) 
    num = subtract_seven(num) 
    print("This is the result after subtracting 7: ", num)

def subtract_seven(num):
    num = num - 7 
    return num

if __name__ == '__main__':
    main()
