def calculate(numbers, value, operation):
    for num in numbers:
        if operation == "add":
            yield num + value
        elif operation == "sub":
            yield num - value
        elif operation == "mul":
            yield num * value

my_list = [10, 20, 30, 40]

print(list(calculate(my_list, 5, "add")))
print(list(calculate(my_list, 5, "sub")))
print(list(calculate(my_list, 5, "mul")))