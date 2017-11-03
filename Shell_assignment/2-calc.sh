#!/bin/sh

############################################################
#
#Program to  implement a basic calculator
#
############################################################

# check if three arguments have been passed
if [ $# -ne 3 ]
	then
	echo "The program needs 3 argumnets"
	echo "Usage: <program.name> add/sub/mul/div arg1 arg2"
	exit
fi

case $1 in
	add) echo $[$2 + $3];;

	sub) echo $[$2 - $3];;

	mul) echo $[$2 * $3];;

	div) echo $[$2/$3];;
		
esac

