def myfun(fx):
    def myfx(*args,**kwargs):
        print("Good morning")
        fx(*args ,**kwargs)
        print("Thanks for showing")
    return myfx
    
@myfun
def hello():
    print("Hello RANA")

@myfun
def add(a,b):
    print("Addition is:",a+b)

hello()
print("--------------------------")
add(20,30)




