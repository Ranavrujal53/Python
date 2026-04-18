class employee():
    language ="python" # this is class attribute
    salary = 100000

harry = employee()
harry.name = "Harry" # this is an object(instance) attribute
print(harry.name,harry.language,harry.salary)

rohan = employee()
rohan.name = "Rohan"
print(rohan.name,rohan.language,rohan.salary)

#here name is object(instance)  attribute an dsalary and language are class attribute as they directly belong to the class
