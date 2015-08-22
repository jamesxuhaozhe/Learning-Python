from sys import argv

script, file_name = argv

print "The file we wanna operate on is called %r" % file_name
print "If you want to abort the operation, please use the command CTRL + C"
print "Otherwise, please hit return"

raw_input("?")

target = open(file_name, 'w')
target.truncate()
line1 = raw_input("Tell us the first line you want to enter?")
line2 = raw_input("Tell us the second line you want to enter?")
line3 = raw_input("Tell us the third line you want to enter?")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print "Now we will close the file..."
target.close()



