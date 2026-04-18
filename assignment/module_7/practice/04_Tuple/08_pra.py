t1 = ("python", 2, 3, True, 3j+6, 3.144, [1,2,3,4], {"name":"raj"}, (1,2,3), {1,2,3,4})

print("Original Values:", t1)

for i in t1:
    print(i, "->", type(i))