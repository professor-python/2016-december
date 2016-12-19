# Декораторы

def decorator(func):
	# Каким-то образом преобразуе5м функцию в новую
	return new_func


def decorator(func):
	def new_func():
		print('Запускается new_func')
		return func() + 1
	return new_func

@decorator # декорирование функции
def some_func():
	print('запускается some_func')
	return max([1, 2, 3, 54, 56])

#new_some_func = decorator(some_func) # запуск декоратора
#print( new_some_func() )
