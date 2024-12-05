class parentclass1:

    def divn(self):
        res = self.a / self.b
        return res

    def test1(self):
        return "india"

    def test2(self):
        return "rama"


class parentclass2:
    def evenorodd(self):
        return self.a % 2

    def rohit(self):
        return "all the best rohit"






class childclass(parentclass1):
    #parent functions will be coming first and then child funcs
    def __init__(self,a,b,c,d,e,f,first,last):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.first = first
        self.last = last

    def addn(self):
        res = self.a + self.b + self.c
        return res

    def subn(self):
        res = self.d - self.e - self.f
        return res

    def mul(self):
        res = self.a * self.c
        return res

    def test2(self):
        return "santhosh"

    def sample(obj1,m,n,p,q):
        res = m + n + p + q
        return res

    def concat(self):
        temp = self.first + " " + self.last
        return temp



obj1 = childclass(50,20,30,60,20,10,"santhosh", "yadav")
obj2 = childclass(5,2,7,8,3,1,"raghu", "gowda")
obj3 = childclass(100,200,400,300,50,70,"rama", "krishna")


print(obj1.a)
print(obj3.c)

res = childclass.addn(obj3)
print("addition res = ", res)


res = childclass.subn(obj2)
print(res)

res = childclass.concat(obj3)
print(res)



### features of oops


# Inheitance :

res = childclass.divn(obj1)
print(res)


# overwriting

res = childclass.test2(obj1)
print(res)


# Overloading or polymorphism

res = childclass.test2(obj1)
print(res)

res = parentclass1.test2(obj1)
print(res)

kk=childclass.test1(obj1)
print(kk)

