
def main():
#input taken from a file "test.txt"
	with open("test.txt") as file:
		data= file.read()
	vowels=0
	for i in data:
		if i in vowelList:
			vowels=vowels+1
	#print (filter(lambda i:i in vowelList,data))
	print ("The Number of Vowels is",vowels)
	print("Enter the vowel whose count is to be checked")
	vowelCount(input(),data)
	
def vowelCount(x,data):
#if the given input is not a vowel
	if x not in vowelList:
		print("Please enter a vowel")
		vowelCount(input(),data)
#if it is a vowel
	else:
		count=0
		for i in data:
			if i==x:
				count =count+1
		print("The count is ",count," Continue or exit: Press 1 or 0")
		if int(input())==1:
			print("Enter the vowel whose count is to be checked")
			vowelCount(input(),data)
	
str='aeiouAEIOU'
vowelList=list(str)	
main()