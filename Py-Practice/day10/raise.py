def enterage(age):
    if age<=0:
        raise ValueError('Only integer more than 0 is allowed')
    elif age%2==0:
        print('Even age')
    else:
        print('Odd age')
try:
 enterage(0)
except ValueError:
    print("Value error")
print("competed!!")