class programmer():
    company = "microsoft"

    def __init__(self,name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode= pincode

r = programmer("Rana",120000,394120)
print(r.name,r.salary,r.pincode,r.company)


c = programmer("chiman",120000,394120)
print(c.name,c.salary,c.pincode,c.company)
