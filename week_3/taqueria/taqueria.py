food={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    sum=0
    while True:
        try:
            choice=input("Item: ").title()
            if choice in food:
                sum+=food[choice]
                print(f"Total ${sum:.2f}")


        except EOFError:
            print("\n")
            break


main()