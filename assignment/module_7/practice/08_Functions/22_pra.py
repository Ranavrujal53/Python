num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))

calc = lambda a, b: (a + b, a * b)
print(calc(num1, num2))