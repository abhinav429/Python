def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif not s[0].isalpha() or not s[1].isalpha():
        return False
    elif s[-1].isdigit() and s[-2].isdigit():
        return False
    elif '0' in s[1:]:
        return False
    elif any(p in s for p in " .,!;:"):
        return False
    return True

main()

