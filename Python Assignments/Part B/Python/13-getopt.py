#! /usr/bin/python3


###################################################################################################################################
#
#
#
#Program to count the number of occurences of word "Embedded" in a input file, and wirte the count to an output file using CLA and getopts'''
#
#
#
############################################################################################################################################



import getopt
import re
import sys

# function to desrcibe the usage to the user 
def usage():
	print ("Usage: 1-getopt.py [-i] [INPUTFILE] [-o] [OUTPUTFILE]")
	sys.exit(0)

def main():
	#to count the number of occurences
	count=0
	# the args list taken from CLA
	args= sys.argv[1:]
	#the argumnets and option list are assigned to args and optlist rspectively
	optlist,args=getopt.getopt(args,'i:o:h',['input','output','help'])
	
	#print (optlist)

	#for each option in optlist
	#it has to be checkd if only input is given without output
	for opt,arg in optlist:
		# for help
		if opt in ('-h','--help'):
			usage()
		#if user specifies an input file , data is read from input file
		elif opt in ('-i','--input'):
			#flag is used to check whether output file is specified
			flag=0
			# to read and count the occurence of the word in input file
			with open(arg) as ar:
				data= ar.read()
				# count occurences using regular expressions
				count= len((re.findall('[Ee]mbedded',data)))
			# again each option in optlist is checked
			for temp_opt,temp_arg in optlist:
				if temp_opt in ('-o','--output'):
					flag=1
			# if no output file specified
			if flag==0:
				usage()

		# if user specifies an output file
		# it should be checked if input file is present before 
		# implementing the logic for output
		elif opt in ('-o','--output'):
			flag=0
			# to check if input file has been specified
			for temp_opt,temp_arg in optlist:
				if temp_opt in ('-i','--input'):
					flag=1
			# if input not present
			if flag==0:
				usage()
			# write to file
			with open(temp_arg,'w') as aw:
				aw.write(str(count))

		else:
			usage()


if __name__ =='__main__':
	main()
