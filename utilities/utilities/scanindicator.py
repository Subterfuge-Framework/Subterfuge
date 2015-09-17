#!/usr/bin/python
import os
import re
import sys
import time
sys.path.append('/usr/share/subterfuge')

pid = sys.argv[1]
target = sys.argv[2]

while True:
   if os.path.exists('/proc/' + str(pid)) == False:
      os.system('python ' + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'utilities/scan.py ' + target)
      break
      
   else:
      time.sleep(.5)
      
