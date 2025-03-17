#single inheritance

class A:
    def m1(self):
        print('m1 method from class A')
class B(A):
    def m2(self):
        print('m2 method from class B')

b=B()
b.m1()#parent class method
b.m2()
print('==============================')
# one more variation
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b=100,200
    def m2(self):
        print(self.b-self.a)

b=B()
b.m1()#parent class method
b.m2()
print(b.x,b.y,b.a,b.b) #accessing parent variables
print('===========================')
#multi-level inheritance
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b=100,200
    def m2(self):
        print(self.b-self.a)
class C(B):
    m,n=10.5,20.9
    def m3(self):
        print(self.m*self.n)

c=C()
c.m1()
c.m2()
c.m3()
print(c.x,c.y,c.a,c.b,c.m,c.n) #accessing parent variables
#heirarchy inheritance
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B(A):
    a,b=100,200
    def m2(self):
        print(self.b-self.a)
class C(A):
    m,n=10.5,20.9
    def m3(self):
        print(self.m*self.n)

print('===========================')
b=B()
c=C()
b.m1()
b.m2()
c.m1()
c.m3()
print(b.x,c.y) #accessing parent variables
#multiple inheritance
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class B():
    a,b=100,200
    def m2(self):
        print(self.b-self.a)
class C(A,B):
    m,n=10.5,20.9
    def m3(self):
        print(self.m*self.n)

print('============multiple===============')
c=C()
c.m1()
c.m2()
c.m3()
print(c.x,c.y,c.a,c.b,c.m,c.n)

