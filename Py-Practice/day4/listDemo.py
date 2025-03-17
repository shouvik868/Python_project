mylist1=[10,20,30,40]
mylist2=['shouvik','rupa','gublu','ram']
mylist3=[10,'shouvik',30,4.75]
mylist4=list()#empty list
print(mylist1)
print(mylist2)
print(mylist3)
print("+_+_+_+_+")
print(mylist4)
print('END!!!')

#accessing items from the list
print(mylist2[2])
print(mylist1[0])
print(mylist3[3])
print(mylist3[-1])# -1 is last element
print(mylist3[-2])# n-2 value

#range of index
print(mylist1[0:2])
print(mylist1[1:4])
print(mylist1[-3:4])

# change value in the list
mylist20=['shouvik','rupa','gublu','ram']
print(mylist20)
mylist20[0]='Navin' #changing 0th position item
print(mylist20)
#list traversal

for i in mylist20:
    print(i)
#check existence of an item

if 'Navin' in mylist20:
    print('yes!!')
else:
    print('No!!')
print(len(mylist20)) #list length
#add new item in list
mylist21=['shouvik','rupa','gublu','ram']
print(mylist21)
mylist21.append('naVin')#way 1 for append at the end
print(mylist21)
mylist21.insert(2,'Disha')#way 2 for append at any index position
print(mylist21)
#Remove item from the list
mylist22=['shouvik','rupa','gublu','ram']
print(mylist22)
mylist22.pop(3)#way 1
print(mylist22)
del mylist22[2] #way 2
print(mylist22)
mylist22.clear()# clear all existing items and return empty list
print(mylist22)
mylist23=mylist22#way 1 copy list
print(mylist23)
mylist23.append('abc')
mylist23.append('def')
mylist23.append('ghi')
print(mylist23)
mylist24=list(mylist23)#way 2 copy list
mylist24.append('jkl')
print(mylist24)
mylist25=mylist24.copy()# way 3 copy list
print(mylist25)
#joining 2 lists
mylist30=mylist24+mylist25# way 1 of joining by concatenation
print(mylist30)
mylist1=['abc','def']
mylist2=[1,2,3]
for i in mylist2:   #way 2 by looping
    mylist1.append(i)
print(mylist1)
# way 3 by extending
mylist1=['abc','def']
mylist2=[1,2,3]
mylist2.extend(mylist1)
print(mylist2)

