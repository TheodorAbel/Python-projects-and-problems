greeting=input("Greeting: ").strip().lower()



greet= True if greeting.startswith("hello") else False

salute= True if greeting.startswith("h") else False




if greet:
    print("$0")
elif salute:
    print("$20")
else:
    print("$100")

