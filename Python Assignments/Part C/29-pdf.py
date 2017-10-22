#################################################
#
# Program to find all the .pdf files in the path 
# given by user
#
############################################

import os
import re
import sys


# ask the user for the path and store it in "path"
path=input("Enter the path where pdf files are to be searched\n")

# extract all files in that path in "items"
items=(os.listdir(path))

# for each file in items, check if it is a pdf
for i in items:
	pdfs=re.findall('pdf$',i)
	if pdfs:
		print (i)


