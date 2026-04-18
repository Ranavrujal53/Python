class Calc:
    def add(self, *numbers):
        return sum(numbers)

c = Calc()
print(c.add(10, 20))
print(c.add(10, 20, 30))

