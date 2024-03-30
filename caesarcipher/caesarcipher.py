import caesar

def main():
    mode = caesar.get_mode()
    key = caesar.get_key()

    if mode == 'E':
        string = caesar.encrypt(caesar.get_string("Enter the message to encrypt"), key)
    elif mode == 'D':
        string = caesar.decrypt(caesar.get_string("Enter the message to encrypt"), key)

    print(string)



if __name__ == "__main__":
    main()