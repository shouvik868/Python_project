myset={'banana','orange','mango'}
print(myset)
for i in myset:
    print(i)
if 'orange' in myset:
    print('Yess!!')
else:
    print('No!!')

print('cherry' in myset) #false
#add
myset.add('cherry')
print(myset)
myset.update(['apple','grape'])
print(myset)
print(len(myset))
#remove
myset.remove('apple')
print(myset)
myset.discard('grape')
print(myset)
myset.clear()
print(myset) #set() but del completely delete the set
myset1={'banana','orange','mango'}
myset2={'cherry','grape','kiwi'}
#joining
#myset3=myset1.union(myset2)
#print(myset3)
myset2.update(myset1)
print(myset2)


