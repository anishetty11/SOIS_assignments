

def main():
	print("Enter the no")
	numb=list(input())
# checking whether the input is a whole number
	assert int(''.join(numb))>-1, 'Enter positive number'
	sum=0
	for i in numb:
		sum=sum+pow((int(i)),len(numb))
	if sum== int(''.join(numb)):
		print ("Armstrong number")
	else:
		print ("Non Armstrong number")
		
main()
	
	