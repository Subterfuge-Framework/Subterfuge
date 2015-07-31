#!/usr/bin/python

import os
import re
import sys
import time



def main():

	#Checks for sane arguments
	if len(sys.argv) != 2:
		usage()
	
	ipaddress = sys.argv[1]	
	os.system('iptables -A FORWARD -s ' + ipaddress + ' -j DROP')	



def usage(): 

	print "\nSubterfuge courtesy of r00t0v3rr1d3 & 0sm0s1z \n"
	print "Usage: dos [IPADDRESS] \n"
	sys.exit(1)
 
if __name__ == '__main__':
	main()				

