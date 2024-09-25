def main():
    while True:
        value = input("Fraction: ")
        try:
            percentage = convert(value)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    if not isinstance(fraction, str):
        raise ValueError("Input must be a string")

    try:
        num1, num2 = fraction.split("/")
        num1 = int(num1)
        num2 = int(num2)
        if num2 == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        if num1 > num2:
            raise ValueError("Numerator cannot be greater than denominator")
        return round((num1 / num2) * 100)
    except ValueError:
        raise ValueError("Invalid input format")

def gauge(percentage):
    if not isinstance(percentage, int):
        raise TypeError("Percentage must be an integer")
    if percentage < 0 or percentage > 100:
        raise ValueError("Percentage must be between 0 and 100")

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
