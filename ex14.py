from sys import argv

script, name = argv
prompt = "> "

print "Hi %s, I would like to ask you some question, lol" % name
print "What is favourite color?"
color = raw_input(prompt)

print "What kind of women do you like the best?"
women = raw_input(prompt)

print "Which city do you live in?"
city = raw_input(prompt)

print """
%r!, your favourite color is %r, and you like %r the best, and you live in the city called %r
""" % (name, color, women, city)



