def even_num():
    for i in range(1, 11):
        yield i * 2

for num in even_num():
    print(num)