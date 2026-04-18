num = int(input("Enter the number of pattern:"))
for i in range(1,num+1):
    for j in range(i):
        print((j+i)%2,end="")
    print()


