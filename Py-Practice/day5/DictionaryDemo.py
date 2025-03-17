#Create
dicEmployee={
        'Name':'Shouvik Biiswas',
        'Role':'Automation Tester',
        'Post':'Lead',
        'Tag':'Yes',
        'Salary':100000
            }
print(dicEmployee)
#access items 1
for i in dicEmployee:
    print(i+':',dicEmployee[i])#way 1
print(dicEmployee.get('Name'))#way 2
#change values in dictionary
dicEmployee['Post']='Manager'
print(dicEmployee)
dicEmployee.update({'Tag':'No'}) #update existing item
print(dicEmployee)
dicEmployee.update({'Position':'Remote'})#update new item or add
print(dicEmployee)
print('========')
for i in dicEmployee.values():#reading 2
    print(i)
print('========')
for i,j in dicEmployee.items():
    print(i,j)
if 'Tag' in dicEmployee:
    print('Exist!!')
else:
    print('No!!')
if 100000 in dicEmployee.values():
    print('Exist!!')
else:
    print('No!!')
print(len(dicEmployee))
#remove item
dicEmployee.pop('Tag')
print(dicEmployee)
del dicEmployee['Position']
print(dicEmployee)
#clear() or del and then dictionary name
dicEmployee.clear()
print(dicEmployee)
#copy dictionary
dicEmployee1={
        'Name':'Rupa Sarkar',
        'Role':'ETL Engineer',
        'Post':'Manager',
        'Tag':'Yes',
        'Salary':600000,
        'Position':'On-site'
            }
dicEmployee2={
        'Name':'Shouvik Biswas',
        'Role':'Automation Tester',
        'Post':'Lead',
        'Tag':'No',
        'Salary':100000,
        'Position':'Off-shore'
            }
dicEmployee3=dicEmployee2
print('Duplicate employee is',dicEmployee3)
dicEmployee4=dicEmployee3.copy()
print('Duplicate 4 employee is',dicEmployee4)