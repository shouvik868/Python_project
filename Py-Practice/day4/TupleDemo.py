mytuple=('apple','banana','cherry')
mytuple1=()#empty tuple
mytuple2=('apple','banana','cherry',1,2.3)
print(mytuple2)
print(mytuple1)
print(mytuple)
print(mytuple[1])
print(mytuple[-1])
print(mytuple[1:3])
#we can not modify,change,remove or insert values as it is immutable
#to change tuple first change it into list then modify and again convert
mylist=list(mytuple)
print(mylist)
mylist.append('orange')
print(mylist)
mytuple=tuple(mylist)
print(mytuple)
#tuple traverse
for i in mytuple:
    print(i)
#item check
if 'orange' in mytuple:
    print('Yes!!')
else:
    print('No!!!')
#length
print(len(mytuple))
mytuple3=mytuple
print(mytuple3)
tuple1=('a','b','c')
tuple2=('d','e','f')
tuple3=tuple1+tuple2
print(tuple3)




