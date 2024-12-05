class myfunc:

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def avg(self):
      self.x + self.y + self.z / 3
      return res


    def test(self):
        return "Santhosh"
from tkinter.font import names

from dictionary import biswajit


class Calc:

    def __init__(self,x,y,z,a,b,c,p,q,m,n,marks):
        self.x = x
        self.y = y
        self.z = z
        self.a = a
        self.b = b
        self.c = c
        self.p = p
        self.q = q
        self.m = m
        self.n = n
        self.marks = marks


    def add(self):
        res = self.x + self.y + self.z
        return res

    def mul(self):
        res = self.a*self.b*self.c
        return res

    def div(self):
        res = self.p/self.q
        return res

    def sub(self):
        res = self.m-self.n
        return res

    def perc(self):
        res = self.marks/600*100
        return res

    def test(self):
        return "Krishna"


obj1 = Calc(10,120,90,5,6,40,23,78,10,9,540)
obj2 = Calc(11,23,46,78,21,57,89,78,32,11,533)
obj3 = Calc(1,2,3,4,5,6,7,8,9,10,435)


res = Calc.add(obj1)
print(res)

res = Calc.sub(obj3)
print(res)

res = Calc.mul(obj2)
print(res)


res =myfunc.avg(obj1)
print(res)

# Over writing
res = Calc.test(obj1)
print(res)

# Overloading
res = myfunc.test(obj1)
print(res)


# class Biswajit:
#     name="mithun"
#     profession="software developer"
#     age=22
#     def rrrr(self):#######its called method
#         print(f"name is {self.name} and profession {self.profession} age {self.age}")
# biswajit=Biswajit()
# biswajit.rrrr()
#
#
# class Biswajit:
#     name="mithun"
#     profession="software developer"
#     age=22
#     def info(self):
#         print(f"name is {self.name} and profession {self.profession} age {self.age}")
# b=Biswajit()#########object
# b.info()
# a=Biswajit()#########object
# a.name="virat"
# a.profession="athletic"
# a.age=34
# a.info()