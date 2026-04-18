class student:
    name = "rana"
    age = 20
    subject = "math"
    
    def to_student(self):
        print(self.name,self.age,self.subject)

s1 = student()
s1.name="Vrujal"

#function calling
s1.to_student()


#crearing new object
s2 = student()
s2.age=50
s2.subject="m.com"
s2.to_student()