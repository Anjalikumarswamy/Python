class Base: 
    def add(self,a, b):
        return a + b

class Derived:
    def add(self,a, b):
        return a + b + 1

b = Base()
d = Derived()
print(b.add(2,3))
print(d.add(2,3))

