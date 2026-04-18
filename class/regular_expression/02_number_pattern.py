import re

pattern = r"^[6-9]\d{9}$"

number = input("Enter phone number: ")

if re.match(pattern, number):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")