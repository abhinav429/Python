def main():
# get input
    inp=input("Fruit: ").lower()
    
    fda={"apple":130,
         "banana":200,
         "mango":150,
         "kiwi":170,
         "papaya":180
    }
    if inp in fda:
        print(fda[inp])
    else:
        print("Not present")