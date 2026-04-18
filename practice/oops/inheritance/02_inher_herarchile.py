class person:

    def __init__(self,name,salary):
        self.name =  name
        self.salary = salary
    
    def detail(self):
        print(self.name,self.salary)

class employee(person):

    def __init__(self, name, salary, deparment):
        super().__init__(name, salary)
        self.deparment = deparment

    def detail(self):
        print(self.deparment)
        super().detail() 

class employee_2(person):
    def __init__(self, name, salary,timing):
        super().__init__(name, salary)
        self.timing= timing

    def detail(self):
        super().detail()
        print(self.timing)

employees = []

n = int(input("How many employees you want to add? "))

for i in range(n):
    print(f"\nEnter details for Employee {i+1}")
    name = input("Enter name:")
    salary = int(input("Enter salary:"))
    dept = input("Enter deparment:")


    data = employee(name,salary,dept)
    employees.append(data)  

print("---- Employees deatil -------")
for data in employees:
    data.detail()

emp = []

n = int(input("How many employees Shift you want to add? "))

for i in range(n):
    print(f"\n Enter the deatils of second type employee{i+1}")
    name = input("Enter the name:")
    salary = int(input("Enter the salary:"))
    time =  input("Enter the sift:")

    data_2 = employee_2(name,salary,time)
    emp.append(data_2)

print("------ Shift detil -------")
for data_2 in emp:
    data_2.detail()
