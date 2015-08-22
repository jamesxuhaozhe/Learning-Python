from sys import argv

script, file_name = argv

txt = open(file_name)

print txt.read()

file_again = raw_input("Please tell me the file you want to open?")

print open(file_again).read()
