from abc import ABC,abstractmethod

class shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

class rectangle(shape):

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class square(shape):
    def __init__(self,sque):
        self.sque = sque

    def area(self):
        return self.sque*self.sque
    
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14*self.radius*self.radius
    
choice = input("Enter the choice(retangle = R,square = S ,circle = C):")
if choice == "R":
    l = int(input("Enter the length:"))
    w = int(input("Enter the Width:"))
    obj = rectangle(l,w)
elif choice == "S":
    s = int(input("Enter the square number:"))
    obj = square(s)

else:

    c = int(input('Enter the number of circle:'))
    obj = circle(c)

print("Area is ",obj.area())
