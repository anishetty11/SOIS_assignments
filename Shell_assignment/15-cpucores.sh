#!/bin/sh

############################################################
#
#Program to check no of cores, Virtualization support,
# if and mac address
#
############################################################

# cup cores
lscpu | grep "^CPU(s):"
echo
lscpu | grep "Core(s)"
echo


# virtualization support 
vt=` lscpu | grep Virtualization `
if [ "$vt" != null ]
    then
    echo $vt
    echo
else
    echo No virtualization support
    echo
fi


ipdetails=`ifconfig | grep -B1 Bcast`


# mac address
re="HWaddr(.*) inet"
if [[ $ipdetails =~ $re ]]
	then
	echo "Hardware Address:${BASH_REMATCH[1]}"
fi


#ip address
re="inet addr(.*)B"
if [[ $ipdetails =~ $re ]]
	then
	echo "IP address${BASH_REMATCH[1]}"
fi
