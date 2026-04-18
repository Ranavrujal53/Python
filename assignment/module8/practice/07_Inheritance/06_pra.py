class person:
    def __init__(self,name):
        self.name = name

class student(person):
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age

    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)

s=student("Rana",20)

s.show()