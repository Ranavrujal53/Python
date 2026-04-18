class person:
    def __init__(self,name,salary):
        self.name = name
        self.salary =salary
    
    def display(self):
        print(self.name,self.salary)

class employee(person):

    def __init__(self, name, salary,dept):
        super().__init__(name, salary)
        self.dept = dept

    def display(self):
        print(self.dept)
        super().display()

emp = []

n= int(input("Enter the how many employees you want to add? : "))

for i in range(n):

    print(f"Enter the employess detail{i+1}:")

    e_name = input("Enter the name of employee:")
    e_salary =  float(input("Enter the salary of employee:"))
    e_deparment = input("Enter the employee deparment:")

    data = employee(e_name,e_salary,e_deparment)
    emp.append(data)

print("------Employees details--------")
print("\name \t salary \t deparment")
print("=====================================")
for data in emp:
     print(data.name, "\t", data.salary, "\t", data.dept)
    # data.display()






# =======================================================================

# using in the classmethod

# class Person:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary


# class Employee(Person):
#     def __init__(self, name, salary, dept):
#         super().__init__(name, salary)
#         self.dept = dept

#     @classmethod
#     def create_employee(cls):
#         name = input("Name: ")
#         salary = float(input("Salary: "))
#         dept = input("Department: ")
#         return cls(name, salary, dept)

#     def display(self):
#         print(self.name, self.salary, self.dept)


# emp = []

# n = int(input("How many employees? "))

# for i in range(n):
#     print(f"\nEnter employee {i+1} details")
#     emp.append(Employee.create_employee())

# print("\n----- Employee Details -----")
# for e in emp:
#     e.display()
