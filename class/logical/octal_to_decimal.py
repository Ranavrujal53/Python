binary = int(input("Enter a binary number: "))

decimal = 0
power = 0

while binary > 0:
    digit = binary % 10
    decimal = decimal + digit * (8 ** power)
    binary = binary // 10
    power += 1

print("Decimal value:", decimal)