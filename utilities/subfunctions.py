import os

def statuscheck():
   command = "ps -A 1 | sed -e '/arpmitm/!d;/sed -e/d;s/^ //;s/ pts.*//'"
   a = os.popen(command)
   reply = a.read()
   if(len(reply)>1):
      status = "on"
   else:
      status = "off"
   command = "ps -A 1 | sed -e '/wpadhijack/!d;/sed -e/d;s/^ //;s/ pts.*//'"
   a = os.popen(command)
   reply = a.read()
   if(len(reply)>1):
      status = "on"
   command = "ps -A 1 | sed -e '/apgen/!d;/sed -e/d;s/^ //;s/ pts.*//'"
   a = os.popen(command)
   reply = a.read()
   if(len(reply)>1):
      status = "on"
   
   return status