import sys
import fileinput 

def input_writer():
	
	for line in fileinput.input("file.txt", inplace = True):
		line = line.replace('stringinfile', 'newstring')
		sys.stdout.write(line)
	fileinput.close()

input_writer()
