
def main():
    while True:
        try:
            feet_input = input("Enter length in feet (or type 'exit' to quit): ")
            if feet_input.lower() == 'exit':
                break
            feet = float(feet_input)
            inches = feet * 12
            print(f"\n{feet} feet is equal to {inches} inches.\n")
        except ValueError:
            print("Please enter a valid number for feet.\n")

if __name__ == '__main__':
    main()
