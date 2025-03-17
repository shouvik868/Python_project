#calling method/function from different module

#Approach 1
'''import CalculatorModule
CalculatorModule.add(2,3)
CalculatorModule.mul(2,3)'''

#Approach 2
'''from CalculatorModule import add,mul
add(2,3)
mul(2,3)'''

#Approach 3
from CalculatorModule import *
div(6,3)