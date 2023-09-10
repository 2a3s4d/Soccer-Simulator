class Profile:

	"""
	Profile name, age

	Attributes:
	name: str; name of the user
	age: nonneg int; age of the user
	"""
	
	def __init__ (self, name, age):
		"""
		Creates a new profile
		"""
		self.name = name
		self.age = age

	def __str__ (self):
		"""
		Prints a that the player won the league
		"""
		self.age = str(self.age)
		return ("%s the year %s old manager has won the league with their team." %(self.name, self.age))


def getAge():
	"""
	Gets the age from the user
	"""
	x = 0
	y = 0
	while x == 0:
		try: #this will see if the age can be converted into an int
			while y == 0:
				age = input("Enter age: ")
				age = int(age)
				if age < 0:
					print ("Please enter valid age")

				else:
					y = 1
			x = 1
			
		except: #if it cannot it will run this code
			print ("Please enter a valid age")

	return age
