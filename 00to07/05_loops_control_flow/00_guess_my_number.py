import random

def play_game():
    secret_number = random.randint(1, 99)
    attempts = 0

    print("\n✨ I am thinking of a number between 1 and 99... Can you guess it? ✨\n")

    while True:
        try:
            guess = int(input("🎯 Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("📉 Too low! Try again.\n")
            elif guess > secret_number:
                print("📈 Too high! Try again.\n")
            else:
                print(f"\n🎉 Congrats! You guessed it right! The number was {secret_number}.")
                print(f"🧠 It took you {attempts} attempt(s). Well done!\n")
                break
        except ValueError:
            print("❌ Please enter a valid number!\n")

def main():
    print("=====================================")
    print("       🔢 GUESS MY NUMBER GAME       ")
    print("=====================================")

    while True:
        play_game()
        again = input("🔁 Do you want to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("\n👋 Thanks for playing! See you next time.\n")
            break

if __name__ == '__main__':
    main()
