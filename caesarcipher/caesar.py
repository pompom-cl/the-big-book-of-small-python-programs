ALPHAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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


def encrypt(string, key):
    return ''.join([ALPHAS[(ALPHAS.index(c) + key) % 26] for c in string])


def decrypt(string, key):
    return ''.join([ALPHAS[(ALPHAS.index(c) - key) % 26] for c in string])