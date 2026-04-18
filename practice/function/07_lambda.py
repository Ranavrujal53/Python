# add = lambda a, b: a + b
# print(add(10, 120))


a=int(input("Enter the first number:"))
b=int(input('Enter the second number:'))

max_num = lambda a,b : a if a>b else b
print("largest number: ",max_num(a,b))