sum = 0
for num in range(3, 101):
    prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            prime = False
            break

    if prime:
        sum += num

        print("sum of prime number: ",sum)
    #     print(f"{num} is prime")
    # else:
    #     print(f"{num} is not prime")
