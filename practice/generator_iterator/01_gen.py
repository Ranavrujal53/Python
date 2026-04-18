def my_gen():
    yield 1
    yield 2
    yield 3
for x in my_gen():
    print(x)
