 #importing from package
#approach 1
import sys
sys.path.append('C:/Users/HP/PycharmProjects/PythonTraining/day9/pack1')


'''import module1
module1.display() #This is display from module 1
import module2 #This is show from module 2
module2.show()'''

from module1 import*
from module2 import*
display() #This is display from module 1
show() #This is show from module 2