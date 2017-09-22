#! /usr/bin/python3


##########################################################################################################################
#
#
# Program to find the square of a number, area of a rectangle, triangle and circle
#
#
####################################################################################################



def main():
	number=int(input("Enter the number whose square is to be calculated\n"))
	# lambda function o obtain the square of a number
	square= lambda x: x**2
	print ("The square of ",number, "is",square(number))

	length,breadth=map(int,input("Enter the sides of rectangle whose area is to be calculated\n").split())
	# lambda function to obtain the product of two numbers
	area=lambda x,y:x*y
	#the area is calculated by feeding lenght and breadth to the lambda function
	print ("The area of rectangle is",area(int(length),int(breadth)))

	base,height=map(int,input("Enter the base and height of triangle whose area is to be calculated\n").split())
	#the area is calculated by feeding lenght and breadth to the lambda function "area", and then halving it
	print ("The area of triangle is",area(int(base),int(height))/2)

	radius=int(input("Enter the radius of circle whose area is to be calculated\n"))
	# the area is calculate by calculating the square using lambda function "squarre", and then multiply by 3.14
	print ("The area of the circle is",(square(radius))*3.14)




main()
