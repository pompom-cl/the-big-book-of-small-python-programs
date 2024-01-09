import sys


def main():
    image = []
    if len(sys.argv) != 2:
        sys.exit('give 1 argument')
    try:
        with open(sys.argv[1]) as file:
            image = file.readlines()
    except FileNotFoundError:
        sys.exit('file not found')
    for i in range(len(image)):
        image[i] = image[i][:-1]
    print("Bitmap Message, by Al Sweigart al@inventwithpython.com")
    print("Enter the message to display with the bitmap.")
    message = input('> ')
    print()
    modulo = len(message)
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] != ' ':
                print(message[j % modulo], end='')
            else:
                print(' ', end='')
        print()


if __name__ == "__main__":
    main()
