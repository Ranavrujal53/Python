count = 0

for num in range(10, 1000):
    temp = num
    sum = 0
   

    while num != 0:
        rem = num % 10
        sum = sum + (rem ** 3)
        num = num // 10

    if temp == sum:
        print(temp)
        count += 1

print("Total Armstrong number:", count)
