class student:

    __id = 18

    def set(self,id):
        self.__id =id

    def get(self):
        print(self.__id)


s = student()
s.set(20)
s.get()