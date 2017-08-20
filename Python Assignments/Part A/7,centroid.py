# taking the input as a dynamic array 
import sys
def main(*arg):
	args=arg[0]
	assert args[0]!=args[2] and args[1]!=args[3],' vertices can\'t have same con_ordinates'
	assert args[0]!=args[4] and args[1]!=args[5],' vertices can\'t have same con_ordinates'
	assert args[4]!=args[2] and args[5]!=args[3],' vertices can\'t have same con_ordinates'
	print('The centroid of the triangle is ',(int(args[0])+int(args[2])+int(args[4]))/3,(int(args[1])+int(args[3])+int(args[5]))/3)

print ("Enter the co_oridintes of three vertices : x1,y1,x2,y2,x3,y3")	
main(input().split())
		
		