age = int(input("Enter your age:"))
weigth = float(input("Enter your weigth:"))

if age >= 18:
    if weigth >= 50:
        print("eligiable ot donate blood")
    else:
        print("your weigth is less than 50. Not eligiable")
else:
    print("Your age is less than 18. Not eligiable")