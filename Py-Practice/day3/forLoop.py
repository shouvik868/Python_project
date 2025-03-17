#print 1 to 10 in ascending and descending order

'''print('++++++++ascending++++++')
for i in range(1,11):
    print(i)
print('++++++++descending++++++')
for j in range(10,0,-1):
    print(j)'''

print('print all even and odd number between 1 to 20:')

print('in ascending order++++++++++++++++++++||||||')
for i in range(1,21):
    print('{} is even and in rage of 1 to 20'.format(i)) if i%2==0 else print('{} is an odd number and in rage of 1 to 20'.format(i))
print('in descending order++++++++++++++++++++||||||')
for j in range(20,0,-1):
    print('{} is even and in rage of 1 to 20'.format(j)) if j%2==0 else print('{} is an odd number and in rage of 1 to 20'.format(j))
