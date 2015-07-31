import os
import sys
sys.path.append('/usr/share/subterfuge/utilities')
  #Ignore Deprication Warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
    #Django Web Modules
from django.template import Context, loader
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.template import RequestContext
from django import forms

    #Database Models
from subterfuge.main.models import *
from subterfuge.modules.models import *
    #Additional Views
from subterfuge.cease.views import *
from subterfuge.modules.views import *

from subfunctions import statuscheck


@csrf_protect
@never_cache
def index(request):
   if request.is_ajax():
      #Get Creds from DB
      creds = credentials.objects.all()
      from subterfuge.modules.models import sessions
      sessions = sessions.objects.all()
   
      #Reset Injection Counter
      iptrack.objects.update(injected = "0")
   
      #Check Arpspoof status
      status = statuscheck()
      
      #Get Info
      modules = installed.objects.all()
      alerts  = notification.objects.all()
      vector = vectors.objects.all()
      
         
         #Relay Template Variables
      return render_to_response("includes/credtable.inc", {
         "credential" :   creds,
         "sessions"   :   sessions,
         "status"	    :	  status,
         "modules"    :   modules,
         "vectors"    :   vector,
         "alerts"	    :   alerts
      })
   else:            
         #Check Attack status
      status = statuscheck()
   
   
         #Get Current Settings from DB
      settings = setup.objects.all()
      modules = installed.objects.all()
      vector = vectors.objects.all()
               
         #Relay Template Variables
      return render_to_response("home.ext", {
         "status"    :   status,
         "setup"     :   settings,
         "vectors"   :   vector,
         "modules"   :   modules,
      })


def notifications(request):
   if request.is_ajax():
    #Get Creds from DB
      creds = credentials.objects.all()
   
         #Reset Injection Counter
      iptrack.objects.update(injected = "0")
   
    #Check Arpspoof status
      status = statuscheck()
   
      alerts   = notification.objects.all()

      
         
         #Relay Template Variables
      return render_to_response("includes/notificationtable.inc", {
         "credential"   :   creds,
         "status"	      :	 status,
         "alerts"	      :   alerts
      })
   else:            
         #Check Attack status
      status = statuscheck()
   
         #Get Current Settings from DB
      settings = setup.objects.all()
       
               
         #Relay Template Variables
      return render_to_response("notifications.ext", {
         "status"    :   status,
         "setup"     :   settings
      })
        
        
def plugins(request):
    if request.is_ajax():
        print "AJAX REQUEST!"
    else:
      		#Read in Config File
        f = open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r')
        config = f.readlines()
        
        modules = installed.objects.all()
                   
            #Relay Template Variables
        return render_to_response("plugins.ext", {
            "config"    :   config,
            "modules"   :   modules,
        })

def hostcheck(request):
    if request.is_ajax():
      		#Read in Config File
        f = open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r')
        config = f.readlines()
        
        		#Check ARP Poison status
        command = "ps -A 1 | sed -e '/arpmitm/!d;/sed -e/d;s/^ //;s/ pts.*//'"
        a = os.popen(command)
        reply = a.read()
        if(len(reply)>1):
        	status = "on"
        else:
        	status = "off"
        
        modules = installed.objects.all()
        client  = iptrack.objects.exclude(id = "1").all()
        scanout = scan.objects.all()
        alerts   = notification.objects.all()
        for data in alerts:
         pass
        notification.objects.update(status = "old")
   

           #Relay Template Variables
        return render_to_response("includes/hostcheck.inc", {
            "config"    :   config,
            "modules"   :   modules,
            "client"    :   client,
            "scan"      :   scanout,
            "status"	   :   status,
            "alerts"	   :   alerts
        })        
        
def netview(request):
    if request.is_ajax():
      		#Read in Config File
        f = open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r')
        config = f.readlines()
        
        		#Check ARP Poison status
        command = "ps -A 1 | sed -e '/arpmitm/!d;/sed -e/d;s/^ //;s/ pts.*//'"
        a = os.popen(command)
        reply = a.read()
        if(len(reply)>1):
        	status = "on"
        else:
        	status = "off"
        
        modules = installed.objects.all()
        client  = iptrack.objects.exclude(id = "1").all()
        scanout = scan.objects.all()

        
           #Relay Template Variables
        return render_to_response("includes/netview.inc", {
            "config"    :   config,
            "modules"   :   modules,
            "client"    :   client,
            "scan"      :   scanout,
            "status"	:   status,
        })
        
    else:
      		#Read in Config File
        f = open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r')
        config = f.readlines()


		       #Check ARP Poison status
        command = "ps -A 1 | sed -e '/arpmitm/!d;/sed -e/d;s/^ //;s/ pts.*//'"
        a = os.popen(command)
        reply = a.read()
        if(len(reply)>1):
        	status = "on"
        else:
        	status = "off"
        
        modules = installed.objects.all()
        client  = iptrack.objects.exclude(id = "1").all()
        scanout = scan.objects.all()

            #Get Current Settings from DB
        settings = setup.objects.all()
        
           #Relay Template Variables
        return render_to_response("netview.ext", {
            "config"    :   config,
            "modules"   :   modules,
            "client"    :   client,
            "scan"      :   scanout,
            "status"	:   status,
            "setup"	:   settings,
        }) 
        

def netctrl(request, cmd):
    if request.is_ajax():

        if cmd == "scan":
            address = request.POST["target"]
            os.system("python " + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + "utilities/scan.py " + address + " &")

        if cmd == "expand":
            iptrack.objects.filter(address = request.POST["address"]).update(expand = "1")

        if cmd == "shrink":
            iptrack.objects.filter(address = request.POST["address"]).update(expand = "0")

      		#Read in Config File
        f = open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r')
        config = f.readlines()
        
        
        modules = installed.objects.all()
        client  = iptrack.objects.exclude(id = "1").all()
        scanout = scan.objects.all()
        
           #Relay Template Variables
        return render_to_response("mods/netview.mod", {
            "config"    :   config,
            "modules"   :   modules,
            "client"    :   client,
            "scan"      :   scanout,
        }) 
        
    else:
                   
            #Relay Template Variables
        return render_to_response("netview.ext", {
            "config"    :   "um",
        })    
        
        
        
        #Writes to the Config File are handled here
def conf(request, module):
      # Read in subterfuge.conf
   with open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r') as file:
      conf = file.readlines()

      # Subterfuge Settings Configuration
      # Edit subterfuge.conf
   if module == "settings":
         #Attack Setup
      try:
         setup.objects.update(iface = request.POST["iface"])
         conf[15] = request.POST["iface"] + "\n"
         print "Using Interface => " + request.POST["iface"]
      except:
         pass
      
      try:
         if request.POST["auto"] == "true":
            setup.objects.update(autoconf = "yes")
            conf[20] = "yes" + "\n"
            print "Auto Configure  => yes"
         else:
            setup.objects.update(autoconf = "no")
            conf[20] = "no" + "\n"
            print "Auto Configure  => no"
      except:
         pass
         
      try:
         setup.objects.update(gateway = request.POST["agw"])
         conf[17] = request.POST["agw"] + "\n"
         print "Using Gateway   => " + request.POST["agw"]
      except:
         pass

      try:
         setup.objects.update(proxymode = request.POST["proxymode"])
         print "Using Gateway   => " + request.POST["proxymode"]
      except:
         pass
         
      try:
         setup.objects.update(gateway = request.POST["mgw"])
         conf[17] = request.POST["mgw"] + "\n"
         print "Using Gateway   => " + request.POST["mgw"]
      except:
         pass

         #Get the Local IP Address
      try:
         f = os.popen("ifconfig " + request.POST["iface"] + " | grep \"inet addr\" | sed -e \'s/.*addr://;s/ .*//\'")
         temp2 = ''
         temp3 = ''
         temp = f.readline().rstrip('\n')
   
         ipaddress = re.findall(r'\d*.\d*.\d*.\d*', temp)[0]
         conf[26] = ipaddress + "\n"
         setup.objects.update(ip = ipaddress)
      except:
         pass
         
         
         #Configuration
      try:
         setup.objects.update(ploadrate = request.POST["ploadrate"])
         setup.objects.update(injectrate = request.POST["injectrate"])
         if request.POST["smartarp"] == "true":
            setup.objects.update(smartarp = "yes")
         elif request.POST["smartarp"] == "false":
            setup.objects.update(smartarp = "no")
         setup.objects.update(arprate = request.POST["arprate"])
      except:
         pass
      
      
         #Vectors
      try:
         if request.POST["active"] == "true":
            vectors.objects.filter(name = request.POST["vector"]).update(active = "yes")
         else:
            vectors.objects.filter(name = request.POST["vector"]).update(active = "no")
            
            #Wireless AP Generator Settings 
         if request.POST["vector"] == "ARP Cache Poisoning":
            arppoison.objects.update(target = request.POST["target"])
            arppoison.objects.update(method = request.POST["arpmethod"])
         
            #Wireless AP Generator Settings
         if request.POST["vector"] == "Wireless AP Generator":
            apgen.objects.update(essid = request.POST["essid"])
            apgen.objects.update(channel = request.POST["channel"])
            apgen.objects.update(atknic = request.POST["atknic"])
            apgen.objects.update(netnic = request.POST["netnic"])
      except:
         pass
         
         
         #Advanced
      try:
         scanip = request.POST["scantargetip"]
         print "Importing Nmap scan for: " + scanip
         
            #Get/Write Files
         if request.FILES['scanresults']:
            scanresults = request.FILES['scanresults']
            dest = open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'utilities/scans/' + scanip + '.xml', 'wb+')
            for chunk in scanresults.chunks():
               dest.write(chunk)
            dest.close()
               #Execute Scan
            os.system('python ' + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'utilities/scan.py ' + scanip)
            
               #Relay Template Variables
         return render_to_response("settings.ext", {
            "config"    :   config,
            "conf"      :   str(config[20]).rstrip('\n'),
            "iface"	   :   result,
            "gateway"   :   gw,
            "status"    :   status,
            "setup"     :   currentsetup,
         })    
      except:
         pass
         

   if module == "update":
      os.system('apt-get install subterfuge')

   if module == "exportcreds":
      os.system('python ' + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'exportcreds.py')

      #################################
      #Subterfuge Module Configurations
      #################################
      
   if module == "httpinjection":   
      httpcodeinjection(request, conf)
      
   elif module == "tunnelblock":   
      tunnelblock()
      
   else:
      for mod in installed.objects.all():
         if module == mod.name:
           os.system('python ' + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'modules/' + module + '/' + module + '.py &')
   
              
      #################################
      #  END MODULE CONFIGURATION
      #################################
   
      # Write to subterfuge.conf
   with open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'w') as file:
      file.writelines(conf)
      
      
      # Call Index Page
      # Check Arpspoof status
   command = "ps -A 1 | sed -e '/arpmitm/!d;/sed -e/d;s/^ //;s/ pts.*//'"
   a = os.popen(command)
   reply = a.read()
   if(len(reply)>1):
	   status = "on"
   else:
	   status = "off"
   
   if module == "httpinjection" or module == "tunnelblock":
            #Relay Template Variables
        modules = installed.objects.all()
        return render_to_response("plugins.ext", {
            "modules"   :   modules,
        })
   else:
         #Relay Template Variables
      return render_to_response(request.META['HTTP_REFERER'].split('/')[3] + ".ext", {
         "status"    :   status,
      })
        
def settings(request):
    if request.is_ajax():
        print "AJAX REQUEST!"

    else:            
	      #Get Interfaces
      f = os.popen("ls /sys/class/net/")
      temp = ''
      temp = f.readline().rstrip('\n')
      result = []
      result.append(temp)
      while (temp != ''):
        temp = f.readline().rstrip('\n')
        if (temp != 'lo'):
           result.append(temp)
      result.remove('')
        
         #Get Gateway
      gw = []
      e = os.popen("route -n | grep 'UG[ \t]' | awk '{print $2}'")
      ttemp = ''
      ttemp = e.readline().rstrip('\n')
      if not ttemp:
         print 'No default gateway present'
      else:
         gw.append(ttemp)
         temp = ''
         gw.append(temp)
         for interface in result:
           f = os.popen("ifconfig " + interface + " | grep \"inet addr\" | sed -e \'s/.*addr://;s/ .*//\'")
           temp2 = ''
           temp3 = ''
           try:
		        temp = f.readline().rstrip('\n')
		        temp2 = re.findall(r'\d*.\d*.\d*.', temp)
           except:
              "No default gw on " + interface
           try: 
              if not temp2:
                 print "No default gw on " + interface
              else:
                 gate = temp2[0] + '1'
                 gw.append(gate)
                 gw.remove('')
                 gw.reverse()
           except:
              print "Something went wrong when determining network gateway information"
              os.system("python /usr/share/subterfuge/utilities/notification.py 'Gateway Error' 'Subterfuge was unable to detect a default gw on any of your interfaces. Sorry.'")
              
            #Read in Config File
      f = open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r')
      config = f.readlines()
        
     
           	#Check Arpspoof status
      command = "ps -A 1 | sed -e '/arpmitm/!d;/sed -e/d;s/^ //;s/ pts.*//'"
      a = os.popen(command)
      reply = a.read()
      if(len(reply)>1):
            status = "on"
      else:
            status = "off"


      currentsetup = setup.objects.all()
      availablevectors = vectors.objects.all()
      arppoisonsettings = arppoison.objects.all()
           
            #Relay Template Variables
      return render_to_response("settings.ext", {
            "config"    :   config,
            "conf"      :   str(config[20]).rstrip('\n'),
            "iface"	   :   result,
            "gateway"   :   gw,
            "status"    :   status,
            "setup"     :   currentsetup,
            "vectors"   :   availablevectors,
            "arppoison" :   arppoisonsettings,
         })

  
        #Command Definitions:
def startpwn(request, method):
    if request.is_ajax():
      os.system("python " + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + "attackctrl.py " + method +" &")
    else:            
      print "Nope... Chuck Testa!"
        
def stoppwn(request):
    if request.is_ajax():
        print "Ceasing Pwn Ops..."
        cease()
    else:
        print "Nope... Chuck Testa!"
        
def resetpwn(request):
    if request.is_ajax():
        print "Resetting Pwn DB..."
            #For MySQL
        #cmd = "mysql --force harvester -u root -ppass < /harvester/templates/flush.sql"
        cmd = "cp " + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + "/base_db " + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + "/db"
        os.system(cmd)
    else:            
        print "Nope... Chuck Testa!"
        
def gate(request):
   if request.is_ajax():
      print "Loading Default Gateway"
      f = os.popen("ifconfig " + interface + " | grep \"inet addr\" | sed -e \'s/.*addr://;s/ .*//\'")
      temp = ''
      temp2 = ''
      temp3 = ''
      temp = f.readline().rstrip('\n')
      temp2 = re.findall(r'\d*.\d*.\d*.', temp)
      temp3 = temp2[0]
      temp3 = temp3 + '1'
		
	      #Relay Template Variables
      return render_to_response("includes/gateway.inc", {
      "gateway"    :   temp3,
      })
   else:            
      print "Nope... Chuck Testa!"
      
      

        
