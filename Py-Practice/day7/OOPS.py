
#creating class
class OOPS:

    #creating different methods
    def myfunction(self):
        pass
    def myMethod(self):
        print('John!!')

    def returnName(self,name):
        print('Hello ',name)
#creating object of the class
obj1=OOPS()
obj2=OOPS()
#accessing methods
print('+++++++++++++')
obj1.myfunction()#no OP as return pass
obj2.myMethod()#John!!
obj2.returnName('Shouvik')#Hello  Shouvik
class MyClass:
    def m1(self):
        print('This is instance method')
    #defining static method
    @staticmethod
    def m2(self,surname):
        print("Hello ",self,surname) #in static method 'self' is also considered as another argument so we need to pass a parameter for self.
        print('This is static method!!')

objc=MyClass()
objc.m1()#This is instance method
#invoking static method-using class name only.
MyClass.m2('Rupa','Sarkar')#Hello  Rupa Sarkar & This is static method!!

#using class variable we need to use 'self' keyword
class MyClassMath:
    a=10
    b=20
    def add(self):
        print('Addig: ',self.a+self.b)

    def substract(self):
        print('substracting: ',self.b-self.a)

obj = MyClassMath()
print("===============")
obj.add()
obj.substract()



