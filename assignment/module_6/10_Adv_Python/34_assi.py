from functools import reduce

l1 = [1, 2, 3, 4, 5]

sq = reduce(lambda x, y: x * y, l1)

print("Original value:", l1)
print("Product of the numbers:", sq)