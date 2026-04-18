class animal:
    def eat(self):
        print("animal can eat")

class dog(animal):
    def bark(self):
        print("dog can bark")

class cat(animal):
    def meow(self):
        print("cat can meow")

d = dog()
c = cat()
print("\nThis is the dog")
d.eat()
d.bark()
print("\nThis is cat")
c.eat()
c.meow()