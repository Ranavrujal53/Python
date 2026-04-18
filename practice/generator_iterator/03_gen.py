def even_number(n):
    for i in range(1,n+1):
        if i % 2 == 0:
            yield i
n=int(input("Enter the number:"))
for num in even_number(n):
    print(num)