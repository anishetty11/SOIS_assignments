
#! /usr/bin/python3


###################################################################################################################################
#
#
#
#Program to count the number of occurences of word "Embedded" in a input file, and wirte the count to an output file using CLA and argparse
#
#
#
############################################################################################################################################



import argparse
import re
import sys

#create a parser object
parser=argparse.ArgumentParser("python 14-argparse.py")

#add mandatory arguments to the parser
parser.add_argument('-i','--input',help='specify the input file',required=True)
parser.add_argument('-o','--output',help='specify the output file',required=True)
#parse the arguments, and store it in "args"
args= parser.parse_args()


# to read and count the occurence of the word in input file
with open(args.input) as ar:
	data= ar.read()
	# count occurences using regular expressions
	count= len((re.findall('[Ee]mbedded',data)))
# to wirte the coun into the file
with open(args.output,'w') as aw:
	aw.write(str(count))



