# Наследование

class A:
	name = ''
	#def some_method(self): print('some from A')

class B:
	def some_method(self): print('some from B')

# наследуем класс C от A и B
class C(A, B):
	pass

print( dir( C ) )

C().some_method()

