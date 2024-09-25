import random

def main():
    level=get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if 1<=level<=3:
                return level
        except ValueError:
            pass

def generate_integer(level):
        correct=0
        if level == 1:
            min_num, max_num = 0, 9
        elif level == 2:
            min_num, max_num = 10, 99
        else:
            min_num, max_num = 100, 999
        for _ in range(10):
            if level==1:
                num1=random.randint(min_num,max_num)
                num2=random.randint(min_num,max_num)
            elif level==2:
                num1=random.randint(10,99)
                num2=random.randint(10,99)
            else:
                num1=random.randint(100,999)
                num2=random.randint(100,999)

            guess=0
            while guess<3:
                try:
                    answer=int(input(str(num1)+" + "+str(num2)+" = "))
                    if answer==(num1+num2):
                        correct+=1
                        break
                    else:
                        print("EEE")
                        guess+=1
                except ValueError:
                    pass
            if guess>2:
                print(str(num1)+"+"+str(num2)+"="+str((num1+num2)))
        print("score: ",correct)

if __name__ == "__main__":
    main()
