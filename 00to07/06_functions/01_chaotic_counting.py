import random

DONE_LIKELIHOOD = 0.3  # You can adjust this for more or less randomness

def chaotic_counting():
    for i in range(1, 11):  # count from 1 to 10
        if done():
            return  # stop counting if done() says we're done
        print(i)

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == '__main__':
    main()
