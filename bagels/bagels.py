import random, re

NUM_DIGITS = 3
MAX_GUESSED = 10


def main():
    print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
    
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:  That means:
  Pico       One digit is correct but in the wrong position.
  Fermi      One digit is correct and in the right position.
  Bagels     No digit is correct.
I have thought up a number.''')

    playing = True
    while playing:
        print(f" You have {MAX_GUESSED} guesses to get it")
        secret_num = generate_secret_number()
        for num_guessed in range(MAX_GUESSED):
            guessed_num = int()
            while True:
                print(f"Guess #{num_guessed + 1}:")
                guessed_num = input().strip()
                if re.search(fr"[0-9]{{{NUM_DIGITS}}}", guessed_num):
                    break
                print("Please insert 3 digits")
            print(guessed_num)
            if re.fullmatch(f"{secret_num}", guessed_num):
                print("You got it!")
                winning = True
                break
            elif not re.match(fr"[{secret_num}]", guessed_num):
                print("Bagels")
            else:
                for index in range(NUM_DIGITS):
                    if re.fullmatch(fr"[\d]{{{index}}}{secret_num[index]}[\d]{{{NUM_DIGITS - index - 1}}}",
                                    guessed_num):
                        print("Fermi", end=' ')
                    elif re.match(fr"[\d]*[{secret_num[index]}][\d]*", guessed_num):
                        print("Pico", end=' ')
                print()
        match input("Do you want to play again? (y or else) "):
            case "y":
                print("Let's play again!")
            case _:
                print("Thanks for playing!")
                break


def generate_secret_number():
    digits = list("0123456789")
    secret_number = ''
    for _ in range(NUM_DIGITS):
        secret_number += str(random.choice(digits))
    return secret_number


if __name__ == "__main__":
    main()
