class demo():
    a = 4

obj = demo()
print(obj.a) #prints the class attribute because instace attribute is not present

obj.a=0 #instance attribute is set
print(obj.a) # print the instance attribute because instance attributr is present

print(demo.a) # prints the class attribute
