def main():
    word=input("Input word: ")
    print(shorten(word))




def shorten(word):
    words=""
    for i in word:

        if i in 'aeiouAEIOU':
            words+=i.replace(i,"")
        else:
            words+=i
    return words
if __name__ == "__main__":
    main()
