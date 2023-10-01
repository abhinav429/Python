def main():
    amount_due=50
    print(f"Amount Due: {amount_due}")
    while amount_due>0:
        donation=int(input("Donate please: "))
        if donation in [5,10,25]:
            amount_due-=donation
            print(amount_due)
        else:
            print(amount_due)   
main()
