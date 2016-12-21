# класс Тепловоз и класс Вагон

class Parovoz:
	power = 0
	wheels = 0
	width = 0
	height = 0
	x = 0

	def run(self, x=100): # self - ссылка на себя (на экземпляр)
		print('Внутри x до добавления:', self.x)
		self.x += x
		print('Hello from Parovoz run! My x:', self.x)

p = Parovoz()
p.x = 3
p.run()
print('Снаружи x:', p.x)
p.run(500)
print('Снаружи x:', p.x)


class Vagon:
        wheels = 0
        width = 0
        height = 0
        weight = 0

