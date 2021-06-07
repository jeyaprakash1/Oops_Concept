# constructor example

class Supermarket:
	'''This is my supermarket'''
	def __init__(self,b,p,d=None): #constructor
		self.brand=b
		self.price=p
		self.discount=d


bread = Supermarket('ABC',25,20)
print(bread.brand)
biscuit = Supermarket("PQR",10,25)
print(biscuit.discount)
shampoo = Supermarket("XYZ",5,20)

rice =Supermarket("Seeragachamba",60)
