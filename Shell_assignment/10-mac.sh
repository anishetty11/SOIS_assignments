#!/bin/sh

###########################################################
#
# Program to scan all MAC adresses in the network
#
# Assuming the device has been assigned IP address of mask
# 255.255.255.0
#
###########################################################

# get the ip details
enp3s0=`ifconfig| grep -A 2 "enp3s0" `
#echo $enp3s0

# extract the first three octects of IP address
re="inet addr:(.*)\..* B"
if [[ $enp3s0 =~ $re ]]
	then
		ip=${BASH_REMATCH[1]}
fi

ip="$ip."
echo $ip


# for each ip in that network, request MAC addres
for i in {1..254}
do
	temp_ip="$ip$i"
	arp_result=` arp-scan  $temp_ip`
	mac_format="$temp_ip(.*:[^ ].)"
	
	# each ip sends the details, MAC address has to be extracted from it
	if [[ $arp_result =~ $mac_format ]]
		then
			mac_match=${BASH_REMATCH[1]}
			#echo ********match
			echo $temp_ip : $mac_match
			echo
		fi
	
	
done
