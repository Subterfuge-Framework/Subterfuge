#!/usr/bin/python
import os
import re
import sys
import time
import datetime
import urllib
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

   if os.path.isfile(os.path.dirname(__file__) + '/credentials.txt'):
      pass
   else:
      os.system("touch /usr/share/subterfuge/credentials.txt")

   with open(str(os.path.dirname(os.path.abspath(__file__))) + '/credentials.txt', 'a') as file:
      for cred in credentials.objects.all():
         source        = cred.source
         username      = cred.username
         password      = cred.password
         date          = cred.date
         file.writelines(source + ", " + username + ", " + password + ", " + date + "\n")

if __name__ == '__main__':
    main()	
