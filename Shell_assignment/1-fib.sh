#!/bin/sh

############################################################
#
#Program to calcualte fibonacchi series 
#
############################################################

# first CLA is assigned to k
k=$1

first=0
second=1

echo "0"

# loop until k becomes zero
while [ $k -gt 0 ]
do
	
	temp=$[ $first + $second ]
	second=$first
	first=$temp
	echo $first

	((k=k-1))
done
