class whild:

    def __init__(self,name,heigth):
        self.name = name
        self.heigth = heigth
        # print(self.name,self.heigth)

    def dispaly(self):
        print(self.name,self.heigth)

class animal(whild):
    def __init__(self, name, heigth,gender):
        super().__init__(name, heigth)
        self.gender = gender

    def dispaly(self):
        print(self.gender)
        super().dispaly()

a = animal("lion",50,"male")
a.dispaly()



