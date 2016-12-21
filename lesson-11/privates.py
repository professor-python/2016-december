class Utka:
	def golos(self):
		return 'krya-krya'

class Dog:
	def golos(self):
		return 'gav-gav'

class Cat:
	def golos(self):
		return 'myau-myau'


animals = [Cat(), Dog(), Dog(), Utka()]

for a in animals:
	print( a.golos() ) # полиморфизм в Python
