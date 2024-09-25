file_name=input("File name: ").strip().lower()
def file(file_name):
    if file_name.endswith(".jpeg") or file_name.endswith("jpg"):
        print("image/jpeg")
    elif file_name.endswith(".gif"):
        print("image/gif")
    elif file_name.endswith(".png"):
        print("image/png")
    elif file_name.endswith('txt'):
        print("text/plain")
    elif file_name.endswith("zip"):
        print("application/zip")
    elif file_name.endswith("pdf"):
        print("application/pdf")
    else:
        print("application/octet-stream")


file(file_name)
