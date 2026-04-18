class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class B(A):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    
    def detail(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)

class C(A):

    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)


# Creating Objects
obj1 = B("Rana", 22, 50000)
obj2 = C("Jay", 25, "Male")

print("---- Class B Output ----")
obj1.detail()

print("\n---- Class C Output ----")
obj2.display()
