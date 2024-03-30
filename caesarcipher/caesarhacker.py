import caesar

def main():
    input = caesar.get_string("What's the secret message?")
    for i in range(26):
        print(f"Key #{str(i).ljust(2, ' ')}: {caesar.decrypt(input, i)}")


if __name__ == "__main__":
    main()