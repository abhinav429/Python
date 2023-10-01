def main():
    x = input("TEXT: ")
    first_word = x.split()[0].lower()
    if first_word == "hello" or first_word == "hello,":
        print("0")
    elif first_word.startswith("h"):
        print("20")
    else:
        print("100")

main()
