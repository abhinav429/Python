def main():
    vow="aeiouAEIOU"
    inp=input("Text :")
    newt=""
    for i,c in enumerate(inp):
        if c not in vow:
            newt+=c
        else:
            continue
    print(f"New text: {newt}")    
main()
