class Worker:
	age = 0
	productivity = 0

	# конструктор - выполняется при создании объекта
	def __init__(self, productivity):
		self.productivity = productivity # назначаем продуктивность при создании

	def work(self):
		#self.productivity = 100
		print('Пришел на работу. Моя продуктивность:', self.productivity)
		self.dinner()
		self.go_away()

	def dinner(self):
		print('Обедаю')
		self.productivity -= 50
		print('Моя продуктивность в обед:', self.productivity)
		self.productivity += 50
		print('Моя продуктивность после обеда:', self.productivity)

	def go_away(self):
		self.productivity = 0
		print('Моя продуктивность по уходу с работы:', self.productivity)


for p in [100, 90, 120]:
	w = Worker(p)
	w.work()

#w2 = Worker(120)
#w2.work()

#w3 = Worker(130)
#w3.work()

