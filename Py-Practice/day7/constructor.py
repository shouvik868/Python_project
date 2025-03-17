class MyClass:
    name='John'
    #parameetarise constructor
    def __init__(self,name):
        print(name) #local argument
        print(self.name) #class variable

mc = MyClass('Rupa') #Rupa John
print('================================')
class Employee:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def display(self):
        print('eid',self.eid)
        print('ename', self.ename)
        print('salary', self.sal)

obj_details=Employee(1090,'Shouvik',100000)
obj_details.display(); #it will invoke init constructor
print('=============str constructor===================')
class Employee:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def __str__(self):
        return('EID {}||ENAME {}||Salary {}'.format(self.eid,self.ename,self.sal)) #can only retunr string.
obj_details1=Employee(1090,'Shouvik',100000)
print(obj_details1) #it will invole str constructor # EID 1090||ENAME Shouvik||Salary 100000






