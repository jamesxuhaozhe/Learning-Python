def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def sub(a, b):
	print "SUBING %d - %d" % (a, b)
	return a - b

def mult(a, b):
	print "MULTING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

a = 9
b = 3

print "The result of adding is: %d" % add(a, b)

print "The result of subtraction is: %d" % sub(a, b)

print "The result of mult is: %d" % mult(a, b)

print "The result of divide is: %d" % divide(a, b)

