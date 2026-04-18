l1 = ["apple", "banana", "cherry", "mango", "orange", "kiwi", "watermelon"]
str_input = input("Enter the fruit search:")

for i in l1:
    if i == str_input:
        print("String found in the list")
        break
else:
    print("String not found in the list")