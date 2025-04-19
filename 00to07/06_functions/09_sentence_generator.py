def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        # noun
        print("I am excited to add this " + word + " to my vast collection of them!")
    elif part_of_speech == 1:
        # verb
        print("It's so nice outside today it makes me want to " + word + "!")
    elif part_of_speech == 2:
        # adjective
        print("Looking out my window, the sky is big and " + word + "!")
    else:
        # invalid input
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

def main():
    word = input("Please type a noun, verb, or adjective: ")
    
    while True:
        try:
            part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
            if part_of_speech in [0, 1, 2]:
                break  # Exit the loop if input is valid
            else:
                print("Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input! Please enter 0, 1, or 2.")

    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()
