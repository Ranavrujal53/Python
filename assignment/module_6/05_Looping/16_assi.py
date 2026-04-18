n = int(input("Enter the number of stars:"))
for i in range(n):
    for j in range(i):
        print("*", end="")
    print()