import sys

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
        sys.exit(1)  # Exit with code 1 if the plate is invalid

def is_valid(s):
    # Check if plate starts with at least two alphabetical characters
    if not (s[:2].isalpha() and 2 <= len(s) <= 6):
        return False
    if not s.isalnum():
        return False
    return check_validity(s)

def check_validity(s):
    has_digit = False
    for i, char in enumerate(s):
        if char.isdigit():
            if not has_digit:
                if char == '0':  # No leading zeros in the number part
                    return False
                has_digit = True
        elif has_digit and not char.isdigit():
            return False  # No letters after numbers start
    return True

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.exit(1)
