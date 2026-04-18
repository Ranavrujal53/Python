def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: division by zero is not allowed"

while True:
    print("\nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Thank you for using the calculator")
        break

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            print("Result =", add(num1, num2))
        elif choice == "2":
            print("Result =", sub(num1, num2))
        elif choice == "3":
            print("Result =", mul(num1, num2))
        elif choice == "4":
            print("Result =", div(num1, num2))
    else:
        print("Invalid choice! Please choose a number from 1 to 5.")