import math
def main():
	print("Enter the vertices x and y of the point 1")
	x1,y1=map(int,input().split())
	print("Enter the vertices x and y of the point 2")
	x2,y2=map(int,input().split())
	print("The Euclidan distance between two points is",math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))
	
main()