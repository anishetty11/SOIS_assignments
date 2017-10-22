#################################################
#
# Program to find all the files of a given type
# in the path. Path is given by user thorugh CLI
# and filetype is taken as CLA
#
############################################


import os
import re
import sys

# ask the user for the path and store it in "path"
path=input("Enter the path where pdf files are to be searched\n")

# get the filetype from CLA 
filetype=(sys.argv)[2]

# get all files from sepcified path
items=(os.listdir(path))

# for each file, check if a file is of required filetype
for i in items:
	pdfs=re.findall('%s$'%filetype,i)
	if pdfs:
		print (i)


