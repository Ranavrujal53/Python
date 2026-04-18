class animal:
    def eat(self):
        print("animal can eat")

class dog(animal):
    def bark(self):
        print("Dog can bark")

class puppy(dog):
    def weep(self):
        print("puppy can weep")

p = puppy()

p.eat()
p.bark()
p.weep()