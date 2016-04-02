class harvester:
   def __init__(self):
      import os
      import sys
      sys.path.append("../")
      
   def purgeLogs(self):
      #Purge Logs
      os.system("echo > /usr/share/subterfuge/sslstrip.log")
      os.system("echo > /usr/share/subterfuge/mitmproxy.log")
      os.system("rm /usr/share/subterfuge/harvester.log")
      os.system("touch /usr/share/subterfuge/harvester.log")

   def httpHarvester(self, feed):
      import os
      import sys
      sys.path.append("../")
      import subprocess
      
      package_dir = os.path.dirname(os.path.dirname(__file__)) + '/packages/'
      print "Starting Harvester"
      
      process = subprocess.Popen('python ' + package_dir + 'harvester/http_cred_harvester.py ' + feed + ' &', shell=True)
      
      return process.pid
