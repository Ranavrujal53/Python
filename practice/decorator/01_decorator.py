# Decorator to allow only numbers
def number_only(func):
    def wrapper(value):
        if value.isdigit():  # Check if input is number
            return func(int(value))
        else:
            print("Error: Only numbers allowed")
    return wrapper

# Decorator to allow only characters
def char_only(func):
    def wrapper(value):
        if value.isalpha():  # Check if input is letters
            return func(value)
        else:
            print("Error: Only letters allowed")
    return wrapper

# Function to double a number
@number_only
def double_number(num):
    print("Doubled:", num * 2)

# Function to print letters in uppercase
@char_only
def shout_char(text):
    print("Uppercase:", text.upper())

# User input
user_input = input("Enter number or letters: ")

# Try number first, then letters
double_number(user_input)
shout_char(user_input)
