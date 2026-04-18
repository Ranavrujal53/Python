num = int(input("Enter the number:"))

if num == 2 or num == 3 or num == 5 or num == 7:
    print("This is prime number")
else:
    if num <= 1 or num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        print("Not prime number")
    else:
        print("Prime number")