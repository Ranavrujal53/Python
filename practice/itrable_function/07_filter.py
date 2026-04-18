# number = [23,45,34,56,45,46,774,45356,346,6356]
# result= filter(lambda x:x % 2 == 0,number)
# print("Original list:",number)
# print("Only even number:",list(result))

number = input("Enter the number:")
num1 = list(map(int, number.split()))

even = filter(lambda x: x % 2 == 0, num1)
print(list(even))
