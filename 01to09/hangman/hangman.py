import random
import string
from words import random
import string
from words import words  

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  

    lives = 6
    max_lives = 6

    print("Welcome to Hangman!")

    while len(word_letters) > 0 and lives > 0:
        
        print(f"\nYou have {lives}/{max_lives} lives left. Used letters: {' '.join(used_letters)}")

        word_display = [letter if letter in used_letters else '_' for letter in word]
        print("Current word:", " ".join(word_display))

       
        while True:
            user_letter = input("Guess a letter: ").upper()
            if len(user_letter) != 1:
                print("Please enter a single letter.")
            elif user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    print(f"Good job! '{user_letter}' is in the word.")
                else:
                    lives -= 1
                    print(f"Oops! '{user_letter}' is not in the word.")
                break
            elif user_letter in used_letters:
                print("You have already used that letter. Try again.")
            else:
                print("Invalid character. Please enter a letter.")

    
    if lives == 0:
        print(f"\nYou died, sorry. The word was: {word}")
    else:
        print(f"\nCongratulations! You guessed the word: {word} ")

    play_again = input("Would you like to play again? (yes/no): ")
    if play_again.lower() == "yes":
        hangman()


hangman() 
import words 

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  

    lives = 6

    print("Welcome to Hangman!")

    while len(word_letters) > 0 and lives > 0:
      
        print("\nYou have", lives, "lives left. Used letters:", " ".join(used_letters))

        
        word_display = [letter if letter in used_letters else '_' for letter in word]
        print("Current word:", " ".join(word_display))

       
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"Good job! '{user_letter}' is in the word.")
            else:
                lives -= 1
                print(f"Oops! '{user_letter}' is not in the word.")

        elif user_letter in used_letters:
            print("You have already used that letter. Try again.")

        else:
            print("Invalid character. Please enter a letter.")

   
    if lives == 0:
        print(f"\nYou died, sorry. The word was: {word}")
    else:
        print(f"\nCongratulations! You guessed the word: {word} 🎉")



hangman()
