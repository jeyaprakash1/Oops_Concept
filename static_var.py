# class specific information (static variable)

class Supermarket:
	'''This is my supermarket'''
	manufacturer = "prakash supermarket" #class specific information
	marketer = "PSM"
	def __init__(self,b,p):
		self.brand=b
		self.price=p
		
bread = Supermarket('ABC',25)
bread.manufacturer='Amutham'
print(bread.manufacturer)
shampoo = Supermarket('Sick',25)
print(Supermarket.manufacturer)
