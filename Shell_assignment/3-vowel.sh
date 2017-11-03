#!/bin/sh

############################################################
#
#Program to calcuate the vowels in a string
#
############################################################

# read the string in a variable called k
echo "Enter the string"

read k

# for all vowels
echo "Vowels =`echo $k | tr -cd [aeiou] | wc -c`"

# for each vowels
echo "a =`echo $k | tr -cd a | wc -c`"
echo "e =`echo $k | tr -cd e | wc -c`"
echo "i =`echo $k | tr -cd i | wc -c`"
echo "o =`echo $k | tr -cd o | wc -c`"
echo "u =`echo $k | tr -cd u | wc -c`"


#echo $vowels
