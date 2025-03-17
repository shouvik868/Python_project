#create simple function
def myfunction():
    print('inside function')
myfunction()
#wit parameter
def myfunction2(name):
    print('hello',name)
myfunction2('Shouvik')
#with multiple parameter
print('================')
def functionAdd(a,b):
    return a+b
sum=functionAdd(20,30)
print(sum)
#returning none
def func():
    return
print(func())
#global keyword
xy=100
def myfunc():
    global xy
    print('global variable',xy)
myfunc()
#global variable will only change if we invoke the function
print('++++++++++++++++++++++')
xy=100
def myfunc():
    global xy
    xy=500
    print('global variable',xy)
print(xy)#100
myfunc()#global variable 500
print(xy)#500