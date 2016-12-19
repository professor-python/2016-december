plus = lambda x, y : x + y
print( plus(1, 2) )


lst = [[1, 17], [-200, 300], [25, -600], [0, 33]]
print( sorted(lst) )
print( sorted(lst, key=lambda x: x[1]) )


print( 'by +:', sorted(lst, key=lambda x: x[0]+x[1]) )
print( 'by sum:', sorted(lst, key=lambda x: sum(x)) )

lambda x: x**x
lambda x: x + 1
lambda x: [a for a in range(10)]

print( "lambda:", (lambda x, a: x / a)(10, 20) )

(1) == 1 # равно
(1,) == 1 # не равно


# КСТАТИ ( унарный if )
a, b = 10, 20

# при правде | условие | в противном случае
x = 10 if a < b else 0

for a in lst:
	b = a[0] if a[0] > a[1] else a[0]+a[1]
	print( b )
