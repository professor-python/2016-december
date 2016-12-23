class Worker:
	hours = 0
	def work(self):
		self.hours += 8
		return self.hours

class Security(Worker):
	def work(self):
		print( 'Я охранник, я разгадываю кроссворд' )
		return super().work()

class Secretar(Worker):
	def work(self):
		print( 'Я секретарь, я приношу кофе' )
		return super().work()

class Arhitector(Worker):
	def work(self):
		print( 'Я архитектор, я проектирую дом' )
		return super().work()

class HouseCleaner(Worker):
	def work(self):
		print( 'Я уборщица: "Натоптали тут, ходят..."' )
		self.hours += 4
		return self.hours #super().work()

class Builder(Worker):
	def work(self):
		#super().work() # Запускаем родительский метод
		print( 'Я строитель, я строю Дом' )
		return super().work()

class Prorab(Worker):
	def __init__(self):
		self.workers = [
			Builder(), # делегирования
			Arhitector(),
			HouseCleaner(),
			Security()
		]

	def work(self):
		super(Prorab, self).work() # в python2 только так
		print( 'Я прораб, я ничего не делаю' )
		h = 0
		for w in self.workers:
			h += w.work()
		return self.hours + h

prorab = Prorab()
print( prorab.work() )
