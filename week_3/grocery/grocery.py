
shop=[]
while True:
    try:
        shop.append(input().upper())
    except EOFError:
        shoped=set(shop)
        unique_shop=list(shoped)
        unique_shop.sort()
        for i in unique_shop:
            print(shop.count(i),i)
        break



