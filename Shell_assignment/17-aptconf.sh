
#!/bin/sh

############################################################
#
#Program to set proxy in apt.conf file
#
############################################################

# get proxy address and port from user
echo "Enter the ip address of the proxy server"
read ip
echo "Enter the port number"
read port


# set http,https,ftp and socks porxy
set_proxy()
{
	for i in 1 2 3 4
	do

		echo "Acquire::$1::Proxy \"$1://${@: -2:1}:${@: -1}\" " | cat >> /etc/apt/apt.txt
		shift
	done
}


set_proxy "http" "https" "ftp" "socks" $ip $port
