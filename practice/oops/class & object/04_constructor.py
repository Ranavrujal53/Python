class emp():
    language ="python"
    salary = 120000

    def __init__(self,name,salary,language): #dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am  creating the object")

    def getdata(self): # instance method
        print(self.language,self.salary)

    @staticmethod
    def greet():
        print("Good moring!")

harry = emp("Vruaj",60000,"JavaScript")
# harry.name = "Rana"
print(harry.name,harry.salary,harry.language)
