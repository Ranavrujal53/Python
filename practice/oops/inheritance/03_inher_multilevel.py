class person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age 
        self.gender = gender

class emp(person):
    def __init__(self, name, age, gender,salary,dept):
        super().__init__(name, age, gender)
        self.salary = salary
        self.dept = dept

class manager(emp):
    def __init__(self, name, age, gender, salary, dept,bonus):
        super().__init__(name, age, gender, salary, dept)
        self.bonus = bonus

    def display(self):
        print(self.name,"\t",self.age,"\t",self.gender,"\t",self.salary,"\t",self.dept,"\t",self.bonus)
       

data = []

n = int(input("Enter how many person want you ?"))

for i in range(n):

    print(f"\n Enter the Job deatil of person {i+1}")
    p_name =  input("Enter the name: ")
    p_age = int(input("Enter the age: "))
    p_gender = input("Enter the gender: ")
    p_salary =  float(input("Enter the salary: "))
    p_dept = input("Enter the deparment: ")
    p_bouns = int(input("Enter the bouns: "))

    user = manager(p_name,p_age,p_gender,p_salary,p_dept,p_bouns)
    data.append(user)

print("------------Person Job detail ---------------")
print("\nname \tage \tgender \tsalary \tdeparment \tBonus")
print("=======================================================")
for user in data:
    user.display()


