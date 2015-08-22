def print_one(*arg):
	arg1, arg2 = arg
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_none():
	print "print none"

print_one("James", "Xu")

print_two("James", "Xu")

print_none()
