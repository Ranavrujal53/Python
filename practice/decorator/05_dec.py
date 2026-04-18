# decorator that return value

def clac(vr):
    def myvr(*args,**kwargs):
        result = vr(*args,**kwargs) 
        return result * 5
    return myvr
@clac
def mul():
    return 40
print("Multipliaction is ",mul())
   