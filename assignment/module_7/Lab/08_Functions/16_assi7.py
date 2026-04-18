def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def divsion(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero not allowed"

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

print("\nSelect operands:")
print("1. Addition")
print("2. Subtraction")
print("3. Multipliction")
print("4. Division")

choice = input("\nEnter the choice 1/2/3/4\n")

if choice == "1":
    print("Result =", add(num1, num2))
elif choice == "2":
    print("Result =", sub(num1, num2))
elif choice == "3":
    print("Result =", mul(num1, num2))
elif choice == "4":
    print("Result =", divsion(num1, num2))
else:
    print("Invalid choice")