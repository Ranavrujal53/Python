# To add one item to a set use the add() method.
# my_set={"apple","banana","cherry"}
# my_set.add("orange")
# print(my_set)

# To add items from another set into the current set, use the update() method.
# my_set={"apple","banana","cherry"}
# st={"orange","mango"}
# my_set.update(st)
# print(my_set)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
# my_set={"apple","banana","cherry"}
# st=["kiwi","mango","orange"]
# my_set.update(st)
# print(my_set)


# Remove set items

# To remove an item in a set, use the remove(), or the discard() method.

# my_set={"apple","banana","cherry"}
# my_set.remove("apple")
# print(my_set)

# my_set={"apple","banana","cherry"}
# my_set.discard("banana")
# print(my_set)

# Remove a random item by using the pop() method
# my_set={"apple","banana","cherry","orange","mango"}
# my_set.pop()
# print(my_set)

# The clear() method empties the set
# my_set={"apple","banana","cherry"}
# my_set.clear()
# print(my_set)

# The del keyword will delete the set completely
# my_set={"aplle","banana","cherry","mango"}
# del my_set
# print(my_set)


# Loop items
# my_set={"apple","banana","cherry","mango","orange","watermelon"}
# for st in my_set:
#     print(st)

# my_set={"apple","banana","cherry","mango","orange","watermelon"}
# for st in enumerate(my_set,start=1):
#     print(st)

# my_set={"apple","banana","cherry","mango","orange","watermelon"}
# for index,st in enumerate(my_set,start=1):
#     print(index,st)

# my_set={"apple","banana"}
# color={"red","yellow"}
# for i in my_set:
#     for j in color:
#         print(i,j)

