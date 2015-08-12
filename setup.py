###SUBTERFUGE Setup Script Current as of version 1.1
#Purpose of this script is to install packages required by Subterfuge
#Error messages pertain to packages that may have failed to install properly.
#Final steps configure Subterfuge to run on the local system
#Setup script is configured to run on Kali Linux (tested on version 2.0) but should work on all debian-based systems

import os

#Dependencies

#Scapy
try:
   os.system("apt-get install python-scapy")
except:
   print "[!] Critical package failed to install: python-scapy"

#Python-Twisted
try:
   os.system("apt-get install python-twisted")
except:
   print "[!] Important package failed to install: python-twisted"
   print "[-] python-twisted is required to perform SSL Stripping attacks"

#Python-Django
try:
   os.system("apt-get install python-django")
except:
   print "[!] Critical package failed to install: python-django"

#Arptables
try:
   os.system("apt-get install arptables")
except:
   print "[!] Critical package failed to install: arptables"

#DHCPD
try:
   os.system("apt-get install dhcpd")
except:
   print "[!] Package failed to install: dhcpd"




#Install Subterfuge
try:
   os.system("cp -R ../subterfuge /usr/share/subterfuge")
