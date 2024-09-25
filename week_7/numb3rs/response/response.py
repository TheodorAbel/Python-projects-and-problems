from validator_collection import validators,errors


def main():
    try:
        email=validators.email(input("what's your email: "))
        if email:
            print("Valid")

    except errors.InvalidEmailError:
        print("Invalid")


if __name__=="__main__":
    main()
