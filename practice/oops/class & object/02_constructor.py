class student:

    collage ="ABC"

    def __init__(self,id,name,age,email):
        self.id = id
        self.name = name
        self.age =age
        self.email =email

    def display(self):
        print(self.id,self.name,self.age,self.email,self.collage)

    @classmethod

    def test(cls):
        print(cls.collage)

    @staticmethod
    def sample():
        print("sample calling")

# student.collage = "sdj"
s= student(10,"rana",20,"rana12@gamil.com")
s.display()

student.test()
student.sample()