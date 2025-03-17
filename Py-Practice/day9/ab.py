# importing methods from classes

#Approach 1
import a
import b


obj_a=a.Animal()
obj_b=b.Bird()
obj_a.display() #I like cow
obj_b.display() #I like parrot

#Approach 2

from a import Animal
from b import Bird
obj_a=Animal()
obj_b=Bird()
obj_a.display() #I like cow
obj_b.display() #I like parrot


