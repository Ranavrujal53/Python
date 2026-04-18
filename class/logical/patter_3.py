num=int(input("Enter the number of start:"))

for i in range(num,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()