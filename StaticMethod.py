# static method - using ' @staticmethod '

class Calculator:
	''' My calculator'''
	@staticmethod
	def add(no1,no2):
		print('Result is',no1+no2)

Calculator.add(100,50) 
