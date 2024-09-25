from pyfiglet import figlet_format,Figlet
import sys
figlet=Figlet()
x=figlet.getFonts()
try:
    if len(sys.argv)==3 and (sys.argv[1]=='-f' or sys.argv[1]=='--font'):
        if sys.argv[2] in x:
            text=input("Input: ")
            print(figlet_format(text,font=sys.argv[2]))
        else:
            sys.exit("Invalid font")

    elif len(sys.argv)==1:
        text=input("Input: ")
        print(figlet_format(text))
    else:
        sys.exit("Invalid argument")
except IndexError:
    sys.exit("Invalid argument")




