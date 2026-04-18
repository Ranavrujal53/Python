def myfun(fx):
    def myfx(*agrs,**kwargs):
        print("Function is starting")
        fx(*agrs,**kwargs)
        print("Function is ending")
    return myfx

@myfun
def add(a,b):
    print("Addtion is:",a+b)
    print("Substration is:",a-b)

print("-------Addtion")
add(10,20)
print("++++++++++++++++++++++++++++++++++++++++")
print("-------Substration ")
add(20,40)

