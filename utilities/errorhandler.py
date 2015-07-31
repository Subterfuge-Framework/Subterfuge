#Error Messaging
import os

##############################
#attackctrl.py
def notification_attackctrl(type):
   if type == "init":
      os.system("python /usr/share/subterfuge/utilities/notification.py 'Starting' 'Subterfuge attack initializing...' '' 'hidden'")
   elif type == "arpwatch-no-rmac":
      os.system("python /usr/share/subterfuge/utilities/notification.py 'Startup Error!' 'Encountered an error configuring arpwatch: Router MAC Address Unknown.'")
   elif type == "autoconfig-error":
      os.system("python /usr/share/subterfuge/utilities/notification.py 'Startup Error!' 'Encountered an error configuring attack: Invalid Arguments in autoconfiguration.'")
   elif type == "no-single-target":
      os.system("python /usr/share/subterfuge/utilities/notification.py 'Startup Error!' 'Could not poison single target: no target found!.'")

##############################
#scan.py
def notification_scan(type):
   if type == "path":
      os.system("python /usr/share/subterfuge/utilities/notification.py 'Scan Error!' 'Error executing nmap scan. Is it in your PATH?'")


##############################
#main/views.py
def notification_main(type):
   if type == "init":
      os.system("python /usr/share/subterfuge/utilities/notification.py 'Starting' 'Subterfuge attack initializing...' '' 'hidden'")
