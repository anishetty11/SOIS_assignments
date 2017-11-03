#!/bin/sh

############################################################
#
#Program to set enviromental proxy
#
############################################################


env_data=` cat /etc/environment | grep -v _proxy`

# ask user if proxy has to be removed
echo " Setup No proxy? [y/n]"
read choice 
# if the choice is yes, unset all proxies
if [ $choice = "y" ]
	then
	echo $env_data | cat > /etc/environment
	echo "unset http_proxy" | cat >> /etc/environment
	echo "unset https_proxy" | cat >> /etc/environment
	echo "unset ftp_proxy" | cat >> /etc/environment
	echo "unset socks_proxy" | cat >> /etc/environment
	rm /etc/apt/apt.conf
	exit
fi


# ask if proxy address will be given manually
echo " Setup Manual proxy? [y/n]"
read choice

set_proxy()
{
	# remove exisitng apt.conf file and add the new proxy
	# address and port to apt.conf and /etc/environemt
	rm /etc/apt/apt.conf
	touch /etc/apt/apt.conf
	echo $env_data | cat > /etc/environment
	# while loop in order to add proxies for http,https,ftp and socks
	while [ $# -gt 0 ]
	do 
		if [ $choice = "y" ]
			then
				echo " Enter the IP address for $1 proxy "
				read ip_proxy
				echo " Enter Port number for $1 proxy"
				read port_proxy
			fi
			protocol=`echo $1| cut -f1 -d_`
			echo "export $1=$protocol//$ip_proxy:$port_proxy" | cat >> /etc/environment
			echo "Acquire::$protocol::Proxy \"$protocol:$ip_proxy:$port_proxy\";" | cat >> /etc/apt/apt.conf
	shift
	done
}
set_proxy "http_proxy" "https_proxy" "ftp_proxy" "socks_proxy"

