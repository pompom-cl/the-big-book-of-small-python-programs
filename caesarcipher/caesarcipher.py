ALPHAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    mode = get_mode()
    key = get_key()

    if mode == 'E':
        string = get_string("Enter the message to encrypt")
        text = ''.join([ALPHAS[(ALPHAS.index(c) + key) % 26] for c in string])
    elif mode == 'D':
        string = get_string("Enter the message to decrypt")
        text = ''.join([ALPHAS[(ALPHAS.index(c) - key) % 26] for c in string])

    print(text)


def get_mode():
    while True:
        print("Do you want to (e)ncrypt or (d)ecrypt?")
        mode = input("> ").upper()
        if mode in ['E', 'D']:
            return mode


def get_key():
    while True:
        print("Please enter the key (0 to 25) to use.")
        key = input("> ")
        if key.isdigit():
            if int(key) >= 0 and int(key) <= 25:
                return int(key)


def get_string(message):
    while True:
        print(message)
        string = input("> ").upper()
        if string.isalpha():
            return string


if __name__ == "__main__":
    main()