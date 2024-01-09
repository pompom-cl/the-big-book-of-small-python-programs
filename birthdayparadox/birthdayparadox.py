import datetime
import random


def main():
    print("Birthday Paradox, by Al Sweigart al@inventwithpython.com\nHow many birthdays shall I generate? (Max 100)")
    number_of_birthdays = get_number_of_birthdays()
    print(f"\nHere are {number_of_birthdays} birthdays:")
    birthdays = get_birthdays(number_of_birthdays)
    print_birthdays(birthdays)
    duplicate = get_match(birthdays)

    if duplicate:
        print('In this simulation, multiple people have a birthday on ', end='')
        print_birthdays(list(set(duplicate)))
    else:
        print("There are no matching birthdays.")

    print(f"\nGenerating {number_of_birthdays} random birthdays 100,000 times...")
    input("Press Enter to begin...")
    print("Let's run another 100,000 simulations.")
    total_duplicates = 0
    for i in range(100_000):
        if i % 10_000 == 0:
            print(f"{i} simulations run...")
        duplicate = get_match(get_birthdays(number_of_birthdays))
        if duplicate:
            total_duplicates += 1
    print(f"Out of 100,000 simulations of {number_of_birthdays} people, there was a"
          f"matching birthday in that group {total_duplicates} times. This means "
          f"that {number_of_birthdays} people have a {round(total_duplicates / 100_000 * 100, 2)}% chance of having a "
          f"matching birthday in their group."
          f"\nThat's probably more than you would think!")


def get_number_of_birthdays():
    while True:
        n = input("> ")
        try:
            n = int(n)
        except ValueError:
            print("Please input a number")
        else:
            if n <= 100:
                return n
            print("Please input number <= 100")


def get_birthdays(number_of_birthdays: int) -> list:
    start = datetime.date(2024, 1, 1)
    birthdays = []
    for _ in range(number_of_birthdays):
        number_of_days = datetime.timedelta(random.randint(0, 365))
        birthday = start + number_of_days
        birthdays.append(birthday)
    return birthdays


def print_birthdays(birthdays):
    n = len(birthdays)
    for index in range(n):
        if index == n - 1:
            print(birthdays[index].strftime("%b %e"))
        else:
            print(birthdays[index].strftime("%b %e"), end=', ')


def get_match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    duplicate = []
    for index1, birthday1 in enumerate(birthdays):
        for index2, birthday2 in enumerate(birthdays[index1 + 1:], index1 + 1):
            if birthday1 == birthday2:
                duplicate.append(birthday1)
    return duplicate


if __name__ == "__main__":
    main()
