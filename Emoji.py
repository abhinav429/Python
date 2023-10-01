def main():
    x=input("text:")
    print(f"Replaced text is:{emo(x)}")

def emo(text):
    text=text.replace(":)","🙂")
    text=text.replace(":(","🙁")
    return text
main()

