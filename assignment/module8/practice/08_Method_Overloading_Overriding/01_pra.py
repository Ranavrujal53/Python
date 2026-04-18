class demo:
    def add(self,*args):
        total = 0
        for i in args:
            total += i

        print("Sum =",total)
        
obj = demo()

obj.add(5,10)
obj.add(5,10,20)
obj.add(5,10,20,30)