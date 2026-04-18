class father:
    def father_name(self):
        self.father= input("Enter father's name:")

class mother:
    def mother_name(self):
        self.mother=input("Enter mother's name:")


class chlid(father,mother):
    def show(self):
        print("\n father name:",self.father)
        print("mother name:",self.mother)

c= chlid()

c.father_name()
c.mother_name()

c.show()