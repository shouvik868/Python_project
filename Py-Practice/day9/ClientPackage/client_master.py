import sys
sys.path.append('C:/Users/HP/PycharmProjects/seleniumProject/Py-Practice/day9/PackageEmployee')
sys.path.append('C:/Users/HP/PycharmProjects/seleniumProject/Py-Practice/day9/PackageStudent')
from emp import Employee
from stu import Student
emp=Employee()
stu=Student()
emp.displayEmp() #{'Name': 'Shouvik', 'eid': 10920, 'post': 'Test Lead'}
stu.displayStu() #{'Name': 'Tubai', 'sid': 18, 'class': 'XXI', 'section': 'B'}

