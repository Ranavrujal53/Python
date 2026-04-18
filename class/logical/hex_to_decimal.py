num = input("Enter the hexadecimal number: ").upper()

decimal = 0
power = len(num) - 1
i = 0

while i < len(num):
    digit = num[i]

    if digit.isdigit():
        value = int(digit)
    else:
        value = ord(digit) - 55   # A=10, B=11, ..., F=15

    decimal += value * (16 ** power)
    power -= 1
    i += 1

print("Decimal number =", decimal)
