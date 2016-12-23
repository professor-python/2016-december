class People:

	all = []
	names = {}
	cars = []

	def __init__(self, name, age, cars=()):
		self.name = name
		self.age = age
		self.all.append( self )
		self.cars = list(cars) # создаем новый список

		if name in self.names:
			self.names[name].append( self )
		else:
			self.names[name] = [ self ]

	@staticmethod
	def average_age():
		# return sum( [ p.age for p in People.all ] ) \
		#	/ len( People.all )
		return ( sum( [ p.age for p in People.all ] )
			       / len( People.all ) )

	@classmethod
	def average_2(cls): # 1-ым аргументом идет ссылка на сам класс
		#return ( sum( [ p.age for p in cls.all ] )
		#               / len( cls.all ) )
		return cls.average_for_list(cls.all)

	@classmethod
	def average_by_name(cls, name):
		return cls.average_for_list( cls.names[name] )

	@classmethod
	def average_for_list(cls, lst): # 1-ым аргументом идет ссылка на сам класс
                return ( sum( [ p.age for p in lst ] )
                               / len( lst ) )


	

vasya = People('Vasya', 13)
marina = People('Marina', 20)
vasya = People('Vasya', 55)
vasya = People('Vasya', 30, cars=['Toyota'])

print( 'lst:', People.all == vasya.all )

print( People.average_age() )
print( People.average_2() )
print( 'Average for Vasya:', People.average_by_name('Vasya') )

print('''
all cars: {}
Vasya cars: {}
? == {}
'''.format(People.cars, vasya.cars, People.cars == vasya.cars)
)
