class pen:
    price = 10
    color ="Red"
    company = "Cello"

# function member / method
    def to_write(self):
        print(self.price,self.color,self.company)

p1 = pen()
p1.price =100
p1.color = "black"
p1.to_write()

p2 = pen()
p2.company = "ss"
p2.to_write()
