#try-except-else-finally
try:
 num1,num2=10,5
 #num1,num2=10,0
 result=num1//num2
 print('result is ',result)
except ZeroDivisionError:
    print("division by 0 not possible")
except SyntaxError:
    print("it is a syntax error")
except:
    print('Exception handled')
else:
    print('No exception occurred') #executes only no exception
finally:
    print('program completed') #always executes


