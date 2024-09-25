def main():
    while True:
        value=input("Fraction: ")
        if Division(value):
            num1,num2=value.split("/")
            try:
                num1=int(num1)
                num2=int(num2)
                if num1<=num2:
                    percentage=calculate(num1,num2)
                    if percentage>=99:
                        print("F")
                        break


                    elif percentage<=1:
                        print("E")
                        break

                    else:
                        print(f"{percentage}%")
                        break
            except ValueError:
                pass




def calculate(num1,num2):
    try:
       p=round((float)(num1/num2)*100)
       return p
    except ZeroDivisionError:
        pass

def Division(value):
        for i in value:
            if i=='/':
                return True
        return False


main()



