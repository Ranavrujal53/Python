#single inheritance 
class animal:
    def eat(self):
        print("Animal can eat")


class dog(animal):
    def bark(self):
        print("Dog can bark")

d = dog()

d.eat()
d.bark()