import random
import sys

def main():
    level=check_level()
    game(level)
    sys.exit(0)

def game(level):
    while True:
        guess=check_guess()
        computer_guess=random.randint(1,level)
        if computer_guess==guess:
            print("Just right!")
            break
        elif computer_guess<guess:
            print("Too large!")
        else:
            print("Too small!")

def check_level():
    while True:
        try:
            level=int(input("Level: "))
            if level>0:
                return level
        except ValueError:
            pass

def check_guess():
    while True:
        try:
            guess=int(input("Guess: "))
            if guess>0:
                return guess
        except ValueError:
            pass


main()
