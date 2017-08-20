import math
def main():
	while(1):
		print ('Enter the two sides')
		a,b=map(int,input().split())
		if b<1 or a<1:
			print ("Sides of the traingle should be positive numbers")
			continue
		break
	print ("Hypotenuse is",math.sqrt(a*a+b*b))

main()