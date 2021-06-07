# object method - object specific information

class Student:
	'''All about Student'''
	def __init__(self,name,mark):
		self.name=name
		self.mark=mark
	def display(self):
		print("Hi",self.name)
		print("your mark is",self.mark)
n=input("Enter Name ")
m=int(input("Enter mark "))
std1=Student(n,m)
std1.display()
