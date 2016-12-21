class Worker:
	age = 0 #- атрибут класса и его экземпляров

	def __init__(self, age=132):
		self.age = age

w = Worker()
print(w.age) # 0

Worker.age = 50
print(w.age) # 50

w2 = Worker()
print(w2.age) # 50

print(Worker.age)
