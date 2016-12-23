# Классы - Свойства

class Worker:

	@property
	def some_prop(self):
		return 'Hello from property'

	@property
	def some_prop_2(self):
		if hasattr(self, '_some_prop_2_value'):
			return self._some_prop_2_value
		return 'Hello from property 2'

	@some_prop_2.setter
	def some_prop_2(self, val):
		#log()
		self._some_prop_2_value = val


w = Worker()
print( w.some_prop )

# w.some_prop = '11111' # Ошибка

print( w.some_prop_2 )
w.some_prop_2 = '11111'
print( w.some_prop_2 )

