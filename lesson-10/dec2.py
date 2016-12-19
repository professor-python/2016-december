def sleeper(func):
	def new_func(*args, **kwargs):
		return func(*args, **kwargs) # распаковка аргументов
	return new_func


@sleeper
def plus(a, b):
	return a + b


print( plus(10, 20) )
