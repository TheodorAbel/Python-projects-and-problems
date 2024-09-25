value=input("Expresions: ").strip()

x,y,z=value.split(" ",2)
x=float(x)
z=float(z)

match y:
    case "+":
        print(f"{(x+z):.1f}")
    case "-":
        print(f"{x-z:.1f}")
    case "*":
        print(f"{x*z:.1f}")
    case "/":
        print(f"{x/z:.1f}")

