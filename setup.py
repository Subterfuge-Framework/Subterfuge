#The purpose of this script is to install the packages required by Subterfuge
#Setup script is configured to run on Kali Linux (tested on version 2.0) but should work on all debian-based systems

import sys, subprocess

print "[+] Beginning Subterfuge installation..."

try:
   #Install Dependencies: Scapy, Python-Twisted, Python-Django, Arptables, DHCPD
   ecode = subprocess.call(["apt-get", "update"])
   ecode2 = subprocess.call(["apt-get", "install", "python-scapy", "python-twisted", "python-django", "arptables", "dhcpd"])
   if (ecode != 0 or ecode2 != 0):
      print "[!] An error occurred while attempting to install the required dependencies using apt-get"
      exit(1)

   #Remove previous installation of subterfuge
   subprocess.call(["rm", "-rf", "/usr/share/subterfuge/"])
   subprocess.call(["rm", "-f", "/usr/share/manage.py"])
   subprocess.call(["rm", "-f", "/bin/subterfuge"])

   #Find Parent Directory
   pathlogic = sys.argv[0]
   parentdirectory = './'
   if '/' in pathlogic:
      parentdirectory = pathlogic.rsplit('/', 1)[0]
      parentdirectory += '/'

   #Install Subterfuge directory to proper location
   ecode3 = subprocess.call(["cp", "-R", parentdirectory, "/usr/share/subterfuge/"])

   if (ecode3 != 0):
      print "[!] An error occurred while attempting to copy the Subterfuge directory"
      exit(1)

   #Add Subterfuge startup script to path
   subprocess.call(["mv", "/usr/share/subterfuge/xsubterfuge", "/bin/subterfuge"])
   #Ensure Subterfuge startup script has execute permissions
   subprocess.call(["chmod", "+x", "/bin/subterfuge"])
   #Install Django control file to proper location. Controls the webserver.
   subprocess.call(["mv", "/usr/share/subterfuge/manage.py", "/usr/share/"])

   print "[+] Subterfuge installation completed successfully!"

except:
   print "[!] An unknown error occurred while attempting to install Subterfuge"
   exit(1)
