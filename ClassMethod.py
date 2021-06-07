# class method -using class spesific ' @classmethod '
class office:
	'''My office'''
	noOfHolidays = 10
	@classmethod
	def checkHolidays(cls,branch):
		print('This year our', branch ,  'have',cls.noOfHolidays)

office.checkHolidays('Chennai')
