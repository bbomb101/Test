import os
from sys import argv


print "Welcome to Project D.I.G."
print "------------------------------------"
print "Now saving the entire filesystem...."
print "------------------------------------"

os.system("sudo ls -alR / > filesystem.txt")

num_lines = sum(1 for line in open('myfile.txt'))

for x in range(1, num_lines):
	file = open(“filesystem.txt”,”r”)
	file.readline(x)
	
	file.close()
