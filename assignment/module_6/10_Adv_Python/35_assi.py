l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = list(filter(lambda x: x % 2 == 0, l1))

print("Original value:", l1)
print("Even numbers:", even)