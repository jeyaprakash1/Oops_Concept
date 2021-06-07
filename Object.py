# object creation example

class SuperMarket:
	'''This is my supermarkrt'''
bread=SuperMarket()
bread.brand='ABC' #object specific information
bread.price=25
biscuit=SuperMarket()
biscuit.brand='PQR'
biscuit.price=10
shampoo=SuperMarket()
shampoo.price=5
rice=SuperMarket()
rice.brand="Seeragachamba"
rice.price=60

print(rice.price)
print(biscuit.__dict__)
