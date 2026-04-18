# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# result = reduce(lambda x, y: x + y, numbers)
# print(result)

# from functools import reduce
# number = [1,2,3,4,5,6]
# result=reduce(lambda x,y : x*y,number)
# print(result)

from functools import reduce

numbers = [10, 45, 23, 89, 12]

result = reduce(lambda x, y: x if x > y else y, numbers)
print(result)