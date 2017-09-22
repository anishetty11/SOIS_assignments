#!/usr/bin/python3

####################################################################################################
#
#Program to download a stable version of kernel from kernel.org and then delete it'''
#
#####################################################################################################
import urllib.request
import os


# the kernel image is downloaded from the URL and, is saved in a file called Kernel.tar.gz
urllib.request.urlretrieve("https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.13.2.tar.xz",'StableKernel')

# the file "Kernel.tar.gz" is removed
os.remove('StableKernel')




