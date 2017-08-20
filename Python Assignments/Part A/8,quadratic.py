import math
def main():
	print ('Enter the constants of quadratic equation a,b,c:')
	a,b,c=map(int,input().split())
	assert (b*b-4*a*c)>-1, '\nImaginary Roots\n'
	delta=math.sqrt(b*b-4*a*c)
	print ('The roots of the equation are ', (-b-delta)/(2*a), 'and' , (-b+delta)/(2*a))
	
main()
	