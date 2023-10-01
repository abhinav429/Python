import sys
# Taking a command line argument
if len(sys.argv)!=2:
    print("only one argument allowed. Please try again")
    sys.exit(1)
else:
    inp=sys.argv[1]
    # Checking if the input which is the name of a file contains ".py" in it
    if ".py" not in inp:
        print("Not a file")
        sys.exit(1)
    else:
        import sys

try:
    with open(inp) as f:
        lines = f.readlines()
except FileNotFoundError:
    print("File not found")
    sys.exit(1)

num = 0
for line in lines:
    line = line.strip()  # removing leading and trailing whitespace
    if line.startswith("#") or not line:
        continue  # Skiping comments and blank lines
    else:
        num += 1  # Incrementing counter for all other lines
print(num)
        
    
            
        
        

