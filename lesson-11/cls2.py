class Window:
	width = 100
	height = 200

Window # это "класс"


w = Window() # создание объекта окна - "экземпляр"
#print( dir(Window) )
print( w.width, w.height )

w.width = 300
print( w.width, w.height )

w.height = 500
print( w.width, w.height )

w.x = 1000 # новый аттрибут экземпляра
print( w.x )

Window.y = 2000 # новый атрибут класса
print( w.y )


# lst = list()
# lst.xx = 11 # будет ошибка
