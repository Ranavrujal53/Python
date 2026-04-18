for num in range(3, 101):
    if num > 3:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
