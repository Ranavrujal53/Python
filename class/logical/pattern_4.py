n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    # print spaces
    for s in range(n - i):
        print("  ", end="")
    
    # print stars
    for j in range(i):
        print("* ", end="")
    
    print()
