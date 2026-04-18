def sum_number(n):
    if n == 0:
        return 0
    return n+sum_number(n-1)
num = int(input("Enter the number:"))
print("Sum of number = ",sum_number(num))