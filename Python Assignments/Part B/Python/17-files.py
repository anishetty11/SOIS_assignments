#!/usr/bin/python3


############################################################################################################################
#
#
# To Find the number of Characters, Words and Lines in test.txt as input file, and storing output in output.txt
#
#
##############################################################################################################################


#function to calculate the no of character
def no_of_characters():
	global char_no
	char_no=len(data)

#function to calculate the no of words
def no_of_words():
	global word_no
	word_no=len(data.split())
#function to calculate the no of lines
def no_of_lines():
	global line_no
	line_no=len(data.split('\n'))

def main():
	global data
	# Opening the file 'test.txt' in read mode(default) 
	with open("test.txt") as file:
		#storing the contents of the file in 'data'
		data = file.read()

	no_of_characters()
	no_of_words()
	no_of_lines()
	# Opening the file 'output.txt' in write mode(default) 
	print ("Characters:",char_no,"\nWords:",word_no,"\nLines:",line_no)

#initializing 	golbal variables to dummy values
data='temp'		
char_no=0
word_no=0
line_no=0
main()
		
