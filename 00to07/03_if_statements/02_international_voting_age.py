ALI_AGE: int = 16
AYESHA_AGE: int = 25
USMAN_AGE: int = 48

def main():
    user_age = int(input("How old are you? "))

    if user_age >= ALI_AGE:
        print("You can vote like Ali where the voting age is " + str(ALI_AGE) + ".")
    else:
        print("You cannot vote like Ali where the voting age is " + str(ALI_AGE) + ".")

    if user_age >= AYESHA_AGE:
        print("You can vote like Ayesha where the voting age is " + str(AYESHA_AGE) + ".")
    else:
        print("You cannot vote like Ayesha where the voting age is " + str(AYESHA_AGE) + ".")

    if user_age >= USMAN_AGE:
        print("You can vote like Usman where the voting age is " + str(USMAN_AGE) + ".")
    else:
        print("You cannot vote like Usman where the voting age is " + str(USMAN_AGE) + ".")

if __name__ == '__main__':
    main()
