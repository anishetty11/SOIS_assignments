

def main():
	fruits={}
	appleOrange=[]
	addFruit(fruits)
	for k,v in fruits.items():
		if k== 'oranges' or k =='apples':
			appleOrange.append[v]
	print ("Dictionary=",fruits,"List =",)
	
def addFruit(x):
	print("Enter the fruit name and the quantity")
	name,numb=input().split()
	x[name]=numb
	print ("Add more fruits? y or n")
	if input()=='y':
		addFruit(x)
	#print (x)
main()