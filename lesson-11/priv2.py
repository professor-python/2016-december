class Worker:
	_age = 10 # подразумеваем, что не для общего использования
	__ves = 100 # защищенный аттрибут (переименовывается ~ при создании)

	def get_ves(self):
		return self.__ves # внутри метода атрибуты не переименованы


print(Worker._age)
#print(Worker.__ves)
print( dir(Worker) )

print( Worker().get_ves() )
