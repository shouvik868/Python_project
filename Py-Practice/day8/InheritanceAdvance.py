#method overriding
class A:
    def m1(self):
        print('m1 method from class A')
class B(A):
    def m1(self):
        print('m1 method from class B') # super keyword calls parent entities
        super().m1()

b=B()
b.m1()
print('==================')
b=A() #UP casting
b.m1()
#=================
class A:
    x,y=10,20
class B(A):
    i,j=30,40
    def m1(self,a,b):
        print(a+b) #local
        print(self.i+self.j)#class
        print(self.x + self.y)  # parent class
b=B()
b.m1(2,3)

#override variables
class A:
    x,y=10,20
class B(A):
    i,j,x=30,40,100
    def m1(self):
        print(self.x+self.y)
        print(self.i+ self.j)
        print('with super: ',super().x+self.y)
b=B()
print('==================')
b.m1()
print(b.x)
#overloading methods-1

class Human:
    def sayHello(self,name=None):
        if name is not None:  #is operator
            print('hello ',name)
        else:
            print('hello alien')

hmn=Human()
hmn.sayHello()
hmn.sayHello('Gublu')
#overloading methods-2

class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

cal=Calculation()
print('==================')
cal.add()
cal.add(2)
cal.add(2,3)
cal.add(2,3,4)



