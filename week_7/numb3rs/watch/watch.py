import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern=r'^(?:<iframe)[^>]*src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"[^>]*>(?:</iframe>)$'
    url=re.search(pattern,s)
    if url:
        return (f"https://youtu.be/{url.group(1)}")





if __name__ == "__main__":
    main()
