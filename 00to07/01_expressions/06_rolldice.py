# Simulate rolling two dice, and prints results of each roll as well as the total.

# Starter Code
# def main():
#     print("Delete this line and write your code here! :)")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
import random

def main():
    while True:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2

        print(f"\nYou rolled a {die1} and a {die2}.")
        print(f"Total: {total}")

        again = input("\nRoll again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("\nThanks for playing!")
            break

if __name__ == '__main__':
    main()
