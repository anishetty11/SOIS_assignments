def main():
	while(1):
		print('Enter the base and height of the traingle')
		b,h=map(int,input().split())
		if b<1 or h<1:
			print ("Base and the Height of the traingle should be positive numbers")
			continue
		break
	print ('Area of the triangle is',0.5*b*h)


main()