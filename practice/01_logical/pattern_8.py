num=int(input("Enter the number:"))
for i in range(num):
    for k in range(i+1):
        print("",end="")
        for j in range(num-1):
            print("*",end="")
        print()

num = int(input("Enter the number: "))

for i in range(num, 0, -1):

    # print leading spaces
    for s in range(num - i):
        print(" ", end="")

    # print stars
    for j in range(i):
        print("*", end="")

    print()
