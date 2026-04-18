class animal:
    def sound(self):
        print("animal make sound")

class dog(animal):
    def sound(self):
        print("dog barks")

d=dog()

d.sound()