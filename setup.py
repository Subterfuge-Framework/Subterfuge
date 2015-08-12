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




#Install Subterfuge
try:
   os.system("cp -R ../subterfuge /usr/share/subterfuge")
