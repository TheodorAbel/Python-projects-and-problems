# seasons.py

from datetime import date
import inflect
import sys

def main():
    birthday = input("Date of Birth (YYYY-MM-DD): ")
    try:
        birth_date = parse_date(birthday)
    except ValueError:
        sys.exit("Invalid input")

    minutes = calculate_minutes_since_birth(birth_date)
    minutes_in_words = convert_minutes_to_words(minutes)
    print(f"{minutes_in_words} minutes")

def parse_date(birthday_str):
    try:
        return date.fromisoformat(birthday_str)
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

def calculate_minutes_since_birth(birth_date):
    today = date.today()
    delta = today - birth_date
    minutes = delta.days * 24 * 60
    return minutes

def convert_minutes_to_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes).replace("and", "").replace("  "," ").capitalize()
    if "thous" in words:
        words = words.replace("thous", "thousand")
    return words

if __name__ == "__main__":
    main()
