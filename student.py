with open("student.csv") as file:
    for line in file:
        row=line.strip().split(",")
        print(f"Name:{row[0]} House:{row[1]}")
          
     