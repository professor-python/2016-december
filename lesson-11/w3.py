class Worker:
	# глобавльная область видимости класса = для всех экземпляров
	KRIZIS = False

	def __init__(self, age, prod=100):
		# локальная область видимости экземпляра = только мои значения
		self.age = age
		self.productivity = prod
		#Worker.KRIZIS = 231321

	def work(self):
		return self.calc() / 2 if Worker.KRIZIS else self.calc()

	def calc(self):
		if self.age < 18:
			return 0
		elif 18 <= self.age < 50:
			return self.productivity
		else:
			return 50 * self.productivity / 100

w = Worker(30)
print( w.work() ) 

w.KRIZIS = True #Worker.KRIZIS = True

w2 = Worker(60)
print( w2.work() ) 


print('global KRIZIS', Worker.KRIZIS)
print('local KRIZIS', w.KRIZIS)

