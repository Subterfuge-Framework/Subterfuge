#!/usr/bin/python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import time
import os
import re
import sys
import datetime
sys.path.append('/usr/share/subterfuge')

   #Ignore Deprication Warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

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
from main.models import *

def main():
   
   title = sys.argv[1]
   message = sys.argv[2]
   status = "new"
   troubleshoot = ""
   try:
      troubleshoot = sys.argv[3]
   except:
      pass
   try:
      status = sys.argv[4] #Status = hidden to hide from GUI, but log
   except:
      pass


   now = datetime.datetime.now()
   date = now.strftime("%d-%m-%Y %H:%M")
   logmessage = notification(status = status, title = title, message = message, troubleshoot = troubleshoot, date = date)
   logmessage.save()
        
if __name__ == '__main__':
        main()
