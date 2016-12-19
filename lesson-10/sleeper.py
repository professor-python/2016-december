from datetime import datetime
import time 

def sleeper(func):
	def new_func():
		print('Ждем 3 секунды')
		time.sleep(3)
		func()
	return new_func

@sleeper
def some_func():
	print('some_func')

some_func()
some_func()
