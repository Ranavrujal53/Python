# num=int(input("Enter the number of star:"))
# for i in range(num):
#     for k in range(num-(i+1)):
#         print("",end=" ")
#         for j in range(i+1):
#             print("*",end=" ")
#         print()

num = int(input("Enter the number of stars: "))

for i in range(1, num + 1):

    # print spaces
    for k in range(num - i):
        print(" ", end=" ")

    # print stars
    for j in range(i):
        print("*", end=" ")

    print()



# num = int(input("Enter the number of star: "))

# for i in range(1, num+1):

#     # print spaces
#     for k in range(num - i):
#         print(" ", end=" ")

#     # print stars
#     for j in range(i):
#         print("*", end=" ")

#     print()
