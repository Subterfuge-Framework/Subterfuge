#!/usr/bin/python
import os
import re
import sys
import time

#Subterfuge Database Models
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

from django.db import models
sys.path.append('/usr/share/subterfuge')
from modules.models import *

#Subterfuge Imports
from errorhandler import notification_scan


target = 'unknown'
ports = []
quickos = 'unknown'
operatingsystem = 'unknown'
mac = 'unknown'
hostname = 'unknown'
def main():

        quickos = 'unknown'
        operatingsystem = 'unknown'
        mac = 'unknown'
        hostname = 'unknown'
        if len(sys.argv) < 2:
                print 'Please use IP address of target as an argument.'
                exit()  

        else:           
                target = sys.argv[1]
                print "Scanning: " + target
                os.system('nmap -T4 -F -A ' + target + ' > ' + target)
                if (os.path.exists(target)):
                        f = open(target, 'r')
                        output = f.readlines()
                        for i in output:
                                if (i.find('/tcp') >= 0):
                                        if (i.find('open') >= 0):
                                                temp = i.rpartition('/tcp')
                                                temp2 = temp[0]
                                                temp3 = temp2.rstrip('\n')
                                                ports.append(temp3)     
                                if (i.find('Running:') >= 0):
                                        if (i.find('Windows') >= 0):
                                                quickos = 'win'
                                                temp = i.rpartition(': ')
                                                temp2 = temp[2]
                                                operatingsystem = temp2.rstrip('\n')
                                        elif (i.find('Mac') >= 0):
                                                quickos = 'osx'
                                                temp = i.rpartition(': ')
                                                temp2 = temp[2]
                                                operatingsystem = temp2.rstrip('\n')
                                        elif (i.find('Linux') >= 0):
                                                quickos = 'lnx'
                                                temp = i.rpartition(': ')
                                                temp2 = temp[2]
                                                operatingsystem = temp2.rstrip('\n')
                                if (i.find('Windows') >= 0):
                                        quickos = 'win'
                                if (i.find('Mac') >= 0):
                                        quickos = 'osx'
                                if (i.find('Linux') >= 0):
                                        quickos = 'lnx'
                                if (i.find('MAC Address:') >= 0):
                                        temp = i.rpartition(': ')
                                        temp2 = temp[2]
                                        temp3 = temp2.rpartition(' (')
                                        temp4 = temp3[0]
                                        mac = temp4.rstrip('\n')
                                if (i.find('Nmap scan report for') >= 0):
                                        temp = i.rpartition('for ')
                                        temp2 = temp[2]
                                        temp3 = temp2.rpartition(' (')
                                        temp4 = temp3[0]
                                        hostname = temp4.rstrip('\n')   
                                if (i.find('NetBIOS name:') >= 0):
                                        temp = i.partition(', ')
                                        temp2 = temp[0]
                                        temp3 = temp2.partition('NetBIOS name:')
                                        temp4 = temp3[2]
                                        hostname = temp4
                                if (i.find('OS:') >= 0):
                                        if (i.find('Service Info:') < 0):
                                                temp = i.rpartition('OS: ')
                                                temp2 = temp[2]
                                                operatingsystem = temp2.rstrip('\n')
                                        
                        
                        if (len(hostname) < 1):
                                hostname = 'Unknown'
                        time.sleep(.5)
                        os.system('rm ' + target)
                        print 'target: ' + target
                        print 'ports: '
                        print ports
                        print 'quickos: ' + quickos
                        print 'operatingsystem: ' + operatingsystem
                        print 'MAC: ' + mac
                        print 'hostname: ' + hostname
                        insert(target, ports, quickos, operatingsystem, mac, hostname)
                else:
                        notification_scan("path")
                        print 'Error executing nmap scan. Is it in your PATH?'
                        
                        
   #insert into database
def insert(target, ports, os, osdetails, mac, hostname):
   iptrack.objects.filter(address = target).update(mac = mac, os = os)
      ####ADD CHECK FOR EXISTING RECORD
   log = scan(address = target, ports = ports, osdetails = osdetails, hostname = hostname)
   log.save()
   

if __name__ == '__main__':
                         main()
