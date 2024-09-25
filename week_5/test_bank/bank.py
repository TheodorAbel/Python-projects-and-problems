import sys
def main():
    greeting=input().lower()
    print(value(greeting))

def value(greeting):
    try:
        if greeting.startswith("hello"):
            return 0
        elif greeting.startswith("h"):
            return 20
        else:
            return 100
    except:
        sys.exit(0)
if __name__ == "__main__":
    main()
