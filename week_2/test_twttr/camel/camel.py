case=input("camel Case: ")
snake_case=""
for i in case:
    if i.isupper():
        snake_case+="_"+i.lower()
    else:
        snake_case+=i

print(snake_case)


