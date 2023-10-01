def main():
  x = input("Answer:")
  if x.isdigit() and int(x) == 42:
   print("YES")
  elif x.replace(" ", "-").lower() == "forty-two":
   print("YES")
  else:
   print("NO")

main()
