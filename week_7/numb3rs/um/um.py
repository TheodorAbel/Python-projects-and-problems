import re

def main():
    print(count(input("Text: ")))


def count(s):
    pattern=r"\bum\b|\bUM\b"
    matches=re.findall(pattern,s)
    return len(matches)




if __name__ == "__main__":
    main()
