ALPHAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    mode = get_mode()
    key = get_key()

    if mode == 'E':
        encrypt(get_string("Enter the message to encrypt"), key)
    elif mode == 'D':
        decrypt(get_string("Enter the message to decrypt"), key)

    print()
    input("> ")
    print("Full encrypted text copied to clipboard")
    print()


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


def get_string():



def encrypt(string, key):



def decrypt(string, key)



if __name__ == "__main__":
    main()