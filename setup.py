###SUBTERFUGE Setup Script Current as of version 1.1
#Purpose of this script is to install packages required by Subterfuge
#Error messages pertain to packages that may have failed to install properly.
#Final steps configure Subterfuge to run on the local system
#Setup script is configured to run on Kali Linux (tested on version 2.0) but should work on all debian-based systems

import os
import subprocess

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
   os.system("rm -rf /usr/share/subterfuge/")
   os.system("rm /usr/share/manage.py")
   
   mv = subprocess.call(["cp", "-R", "../subterfuge/", "/usr/share/subterfuge/"])

   if mv == 1:
      print "[!] Critical Error! Subterfuge install error could not stat primary path. Trying secondary"
      print "..."
      subprocess.call(["cp", "-R",  "../Subterfuge/", "/usr/share/subterfuge/"])
      print "[+] Good! Secondary install mechanism succeeded. Installation continuing..."

   elif mv != 0 and mv != 1:
     print "[!!] Fatal installation error. Install aborted: Could not stat path: /usr/share/subterfuge"

   os.system("cp xsubterfuge /bin/subterfuge")
   os.system("chmod +x /bin/subterfuge")
   os.system("cp manage.py /usr/share/")

   print "[-] Cleaning up"

   os.system("rm /usr/share/subterfuge/xsubterfuge")
   os.system("rm /usr/share/subterfuge/manage.py")

except:
   print "[!] Critical Error! Subterfuge configuration failed"
