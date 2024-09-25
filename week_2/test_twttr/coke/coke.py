amount=50
change_owed=0
def main(amount,change_owed):
    while True:
        print("Amount Due:",amount)
        coin=int(input("input coin: "))

        while  (coin!=5 and coin!=10 and coin!=25):
            print("Amount Due:",amount)
            coin=int(input("input coin: "))
        if amount>coin:
            amount=calc_amount(coin,change_owed,amount)
        else:
            change_owed=calc_change(coin,change_owed,amount)
            return change_owed








def calc_amount(coin,change_owed,amount):
    if amount>coin:
        amount=amount-coin
        return amount
def calc_change(coin,change_owed,amount):
        change_owed=coin-amount
        return change_owed


change=main(amount,change_owed)
print("Change Owed:",change)









