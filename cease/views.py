import os
import re
import sys
import time
from subterfuge.main.models import *

    #Die Gracefully
def cease():
	print 'Cleaning up...'
	time.sleep(1)
	os.system("kill -9 `ps -A 1 | sed -e '/arpmitm/!d;/sed -e/d;s/^ //;s/ pts.*//'` 1> /dev/null 2>/dev/null")
	os.system("kill -9 `ps -A 1 | sed -e '/arpwatch/!d;/sed -e/d;s/^ //;s/ pts.*//'` 1> /dev/null 2>/dev/null")
	os.system("kill -9 `ps -A 1 | sed -e '/sslstrip/!d;/sed -e/d;s/^ //;s/ pts.*//'` 1> /dev/null 2>/dev/null")
	os.system("kill -9 `ps -A 1 | sed -e '/harvester/!d;/sed -e/d;s/^ //;s/ pts.*//'` 1> /dev/null 2>/dev/null")
	os.system("kill -9 `ps -A 1 | sed -e '/ftp_password_sniffer/!d;/sed -e/d;s/^ //;s/ pts.*//'` 1> /dev/null 2>/dev/null")
	os.system("kill -9 `ps -A 1 | sed -e '/cookiestealer/!d;/sed -e/d;s/^ //;s/ pts.*//'` 1> /dev/null 2>/dev/null")
	os.system("kill -9 `ps -A 1 | sed -e '/mitmdump/!d;/sed -e/d;s/^ //;s/ pts.*//'` 1> /dev/null 2>/dev/null")
	os.system("killall mitmdump")
	time.sleep(1)
	
		#Get Globals from Database
	for settings in setup.objects.all():
		interface     = settings.iface
		gateway       = settings.gateway
		attackerip    = settings.ip
		routermac     = settings.routermac
		smartarp      = settings.smartarp
	
		#ReARP The Network
	os.system('python ' + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'utilities/rearp.py -r ' + gateway + ' &')

