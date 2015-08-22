from sys import argv

script, file_name = argv

# open the file
current_file = open(file_name)

def print_all(file):
	print file.read()

def print_one_line(line_counter, file):
	print line_counter, file.readline()

def rewind(file):
	file.seek(0)

print_all(current_file)
rewind(current_file)
line_current = 1
print_one_line(line_current, current_file)
line_current = line_current + 1
print_one_line(line_current, current_file)
line_current = line_current + 1
print_one_line(line_current, current_file)
