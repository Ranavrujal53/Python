class stud:
    # atteribute is variable 
    id  = 1
    name = "rana"
    calss = "10"
    price=400

    def to_student(self):
        print(self.id,self.name,self.calss,self.price)

s1 = stud()
s1.id = 2
s1.name="vrujal"
s1.calss = "bca"
s1.price = 500
s1.to_student()

s2 = stud()
s2.id = 3
s2.name="rana"
s2.calss = "mca"
s2.price = 1000
s2.to_student()