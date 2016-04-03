import os
import re
import sys
import time
import warnings

os.system('iptables -F')
os.system('iptables -X')
os.system('iptables -t nat -F')
os.system('iptables -t nat -X')
os.system('iptables -t mangle -F')
os.system('iptables -t mangle -X')
os.system('iptables -P INPUT ACCEPT')
os.system('iptables -P FORWARD ACCEPT')
os.system('iptables -P OUTPUT ACCEPT')
      

#Import DB Libs
from lib.dbmgr import *

#Import Attack Libs
from lib.feeds import *
from lib.metafeeds import *
from lib.consumers import *
from lib.vectors import *


def disableJob(a):
   #Set job status disabled
   pass

def execJob(jid, cmdstring):
   #Build job
   exp = cmdstring.split(";")
   
   try:
      a = exp[1]
   except:
      #No args
      pass
   
   #Invoke Job
   #Invokes the module class and passes a comma delimited argument list
   print "Invoking job: " + str(jid)
   exec exp[0]
   
   #Set job status enabled
   dbmgr().enableJob(jid)

   
def cleanJobs():
   print "Cleaning up..."
   #Pull db job info
   #Gracefully close tasks
   
   print "Happy Hacking!"
   exit()
   
#MITMServer should be spawned as a background process PID tracked in DB and killed on stop (Ctrl-Z)
#Check if MITMServer already running (via jobs?)

a = "0"

#Main Execution
while True:
   #Check settings for active attack components
   jobs = dbmgr().getJobs()

   for job in jobs:      
      #Startup new jobs
      if job[2] == 1 and job[3] == 0:         
         #Spawn new job
         jid = job[0]
         cmdstring = job[4]
         print "Starting new job " + job[1]
         execJob(jid, cmdstring)
         
      #Stop deactivated jobs
      if job[2] == 0 and job[3] == 1:
         print "Stopping job " + job[1]
         
   time.sleep(1)

#Add try/except handler to catch keyboard interrupt and kill all jobs