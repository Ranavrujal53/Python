num = int(input("Enter the number of rows: "))

for i in range(1, num + 1):
    # Print spaces first
    for j in range(num - i):
        print(" ", end="")
    # Print stars with space
    for k in range(i):
        print("*", end=" ")
    print()  # Move to next row
