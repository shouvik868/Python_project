def func(a,b):
    print(a,b)
func(10,20)#positional argument
func(b=10,a=20)#kewyword argument
func(10,b=40)# just remember in case of combination argument positional should come after keyword argument
#function returns tuples
def compare(a,b):
    if a>b:
        return a,b
    else:
        return b,a

print(compare(10,28))#(28, 10)
print(type(compare(13,7)))#<class 'tuple'>