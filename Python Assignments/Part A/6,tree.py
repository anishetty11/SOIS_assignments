'''Assuming that the angle to the top of the tree is taken WRT the ground, 
and not the person's eye level'''
import math
def main():
	print("enter the distance to the tree")
	distance=int(input())
	assert distance>0,"Distance should be a positive number"
	print("enter the angle ")
	angle=int(input())
	assert angle>0 and angle<90, "Angle should be a positive number less than 90"
#converting degree to radian, and gettin the tangent
	print(' The height of the tree is ',(math.tan(math.radians(angle))*distance))
	
main()