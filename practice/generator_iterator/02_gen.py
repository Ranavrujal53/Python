def number(n):
    for i in range(1,n+1):
        yield i

for x in number(5):
    print(x)