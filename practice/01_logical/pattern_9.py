num=int(input("Enter the number:"))
for i in range(num):
    for j in range(i):
        print(num,end="")
        num+=1
    print()