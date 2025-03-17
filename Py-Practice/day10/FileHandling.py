#writing file
file=open('C:/Users/HP/Desktop/new_framework_2024/Python/myfile.txt','w')
file.write("Hello World!!\n")
file.write("This is 'myfile.txt'.\n")
file.write("I am in writing mode.\n")
file.write("I am trying to write on this file.\n")
file.write("Python is my pen!!")
file.close()
#reading file
#all line
print('======================')
file=open('C:/Users/HP/Desktop/new_framework_2024/Python/myfile.txt','r')
print(file.read()) #in string format
file.close()
#first line
print('======================')
file=open('C:/Users/HP/Desktop/new_framework_2024/Python/myfile.txt','r')
print(file.readline())
file.close()
#first all lines
print('======================')
file=open('C:/Users/HP/Desktop/new_framework_2024/Python/myfile.txt','r')
print(file.readlines()) #in list format
file.close()
#appending into the file

file=open('C:/Users/HP/Desktop/new_framework_2024/Python/myfile.txt','a')
file.write("\nThis is appending line 1\n")
file.write("This is appending line 2")
file.close()
print('======================')
file=open('C:/Users/HP/Desktop/new_framework_2024/Python/myfile.txt','r')
print(file.read())
file.close()
