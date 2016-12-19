from datetime import datetime

def log(func):
	def new_func():
		print('{}: {}'.format(datetime.now(), func.__name__))
		func()
	return new_func
	

@log
def some_func():
	print('Запускаем some_func')


some_func()
some_func()
some_func()


import time
time.sleep(3)
