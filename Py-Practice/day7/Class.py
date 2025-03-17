#use of global local and class variable in a single program

a,b=10,20 #global variable
class MyClass:
    i,j=30,40 #class variable
    def add(self,x,y):    #local variable
        F=x + y + self.i + self.j + a + b
        print('Always add 100 + adding given argument',F)
    def onlyaddingGlobal(self):
        print('Adding global variable only..',a+b)


obj1=MyClass()
obj1.add(20,30) #Always add 100 + adding given argument 150
obj1.onlyaddingGlobal() #Adding global variable only.. 30

#making it more interesting :)

a,b=10,20 #global variable
class MyClass:
    a,b=30,40 #class variable
    def add(self,a,b):    #local variable
        F=a + b + self.a + self.b + globals()['a'] + globals()['b']
        print('Always add 100 + adding given argument',F)

obj2=MyClass()
obj2.add(20,30) #Always add 100 + adding given argument 150