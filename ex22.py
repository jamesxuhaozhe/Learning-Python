print "Let's do more practices"

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is note.
"""

print "------------"
print poem
print "------------"

def strange_func(start_value):
	temp_value = 1000 * start_value
	result_first = temp_value * 10
	result_second = temp_value * 100
	result_third = temp_value * 1000
	return result_first, result_second, result_third

start_value = 9

value1, value2, value3 = strange_func(start_value)

print "value1 is: %d" % value1
print "value2 is: %d" % value2
print "value3 is: %d" % value3

print "value1 is %d, value2 is %d, value3 is%d" % strange_func(start_value)

