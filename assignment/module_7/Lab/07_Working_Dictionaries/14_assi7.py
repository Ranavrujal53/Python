keys = ["name", "age", "course", "city"]
values = ["Rana", 21, "Python", "Ahmedabad"]

student = {}

for i in range(len(keys)):
    student[keys[i]] = values[i]

print(student)