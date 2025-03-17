# s='welcome'
# s1=''
# s2=str('Shouvik')
# print(s,s1,s2)

#string is immutable
'''
str1="welcome"
print(id(str1))
str1=str1+' to python'
print(str1)
print(id(str1))

'''

#+ and * in string
str1='Shouvik'
str2='Biswas'
print(str1+str2)
print(str1*3)

#slicing operator []
print(str1[1:3])
print(str1[:6])
print(str1[2:])
print(str1[1:-1])

# ord() and chr()
print(ord('Z')) # returns ASCII  value 90
print(chr(90))
# max min & len
print(str2)
print(max(str2))
print(min(str2))
print(len(str2))
#in and not in operator

print('swa' in str2)
print('swa' not in str2)

# testing string functions
print('++++++++++++')
s='welcome'
print(s.isalnum()) #checks alpha numeric
print(s.isdigit())
print('================+++')
print('for u'.isidentifier()) #valid identifier according to python
print(s.islower())
print(s.isupper())
print('============')
print(' '.isspace())
# finding sub-string

s='welcome to python'
print(s.endswith('thon'))
print(s.startswith('welc'))
print(s.find('come'))
print(s.find('become'))
print(s.count('o'))
print('+++++++++++++:)+++++++++')

# converting functions
s='string is PYTHON'
print(s)
s1=s.capitalize()
print(s1)
s2=s.title()
print(s2)
s3=s.lower()
print(s3)
print(s.upper())
print(s.swapcase())
print(s.replace('ON','IN'))
print(s)






