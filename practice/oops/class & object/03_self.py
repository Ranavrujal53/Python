class emp():
    language = "Python"
    salary = 1200000

    def getdata(self):
        print(f"This language is {self.language}. this salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good moring")

harry = emp()
harry.greet()
harry.getdata()
