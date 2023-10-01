def main():
    equation = input("START: ")
    first, op, third = equation.split()
    first, third = float(first), float(third)

    if op == "+":
        ans = round(first + third, 1)
    elif op == "-":
        ans = round(first - third, 1)
    elif op == "*":
        ans = round(first * third, 1)
    else:
        ans = round(first / third, 1)

    print(f"The answer is {ans}")

main()






