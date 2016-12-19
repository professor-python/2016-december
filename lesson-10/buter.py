def bread(func):
	def new_func():
		print(' =========')
		func()
		print(' =========')
	return new_func

def tomats(func):
	def new_func():
		print(' OOOOOOOOO')
		func()
	return new_func

def plate(func):
	def new_func():
		func()
		print('\_________/')
	return new_func

@plate
@bread
@tomats
def butterbread():
	print(' ~~~~~~~~~')


butterbread()
