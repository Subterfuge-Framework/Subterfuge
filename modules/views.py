import os
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
    #Database Models
from subterfuge.main.models import credentials
from subterfuge.modules.models import *
    #Additional Views
from subterfuge.cease.views import *
from subterfuge.modules.views import *


   # Subterfuge Module Builder
def build(request, modname, description):

      #Create Module Directory
   os.system('mkdir ' + str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'modules/' + modname + '/')

      #Read Default .mods
   with open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'templates/mods/default.mod', 'r') as file:
      default = file.readlines()
      
   with open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'templates/mods/default_settings.mod', 'r') as file:
      defaultsettings = file.readlines()
      print defaultsettings

      #Format for new Module
   default[2] = "$('#pluginconfigbox" + modname + "').hide();\n"
   default[7] = "function show" + modname + "config()\n"
   default[11] = "$('#pluginconfigbox" + modname + "').fadeIn(1000).show();\n"
   default[16] = "<a href = '#" + modname + "'>\n"   
   default[17] = "<div onclick = 'show" + modname + "config()' id = 'plugin' name = '{{plugin}}'>\n"
   default[18] = "<img src = '/static/images/plugins/" + modname + ".png'><br>\n"  
   default[19] = modname      

   
   defaultsettings[0] = "<div id = 'pluginconfigbox" + modname + "'>\n"   
   defaultsettings[1] = description
   defaultsettings[2] = "<a href = '/" + modname + "/' name = 'pset'><div id = 'redbutton' style = 'margin-top: 385px; color: white;'>Start</div></a>\n"


      #Write .mod files
   with open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'templates/mods/' + modname + '.mod', 'w') as file:
      file.writelines(default)
      
   with open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'templates/mods/' + modname + '_settings.mod', 'w') as file:
      file.writelines(defaultsettings)
   
      #Add Module to database
   newmod = installed(name = modname)
   newmod.save()


   # Subterfuge Module Builder
def create(request):

      #Module Name
   modname     = str(request.POST['modname']).strip(" ")
   des = ""

      #Module Description
   try:
      description = request.FILES['description']
      for chunk in  description.chunks():
         des = chunk
   except:
      print "No GUI Description"

      #Create Module Space
   build(request, modname, des)
      
      #Get/Write Files
   if request.FILES['modicon']:
      icon = request.FILES['modicon']
      dest = open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'templates/images/plugins/' + modname + '.png', 'wb+')
      for chunk in icon.chunks():
         dest.write(chunk)
      dest.close()    
      
   if request.FILES['exploitcode']:
      exploitcode = request.FILES['exploitcode']
      dest = open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") +  'modules/' + modname + '/' + modname + '.py', 'wb+')
      for chunk in exploitcode.chunks():
         dest.write(chunk)
      dest.close()
   
      
      #Relay Template Variables
   return render_to_response("home.ext", {
	   "status"    :   "on",
   })


      #################################
      #Subterfuge Modules Section
      #################################
      
def builder(request): 
	   # Read in subterfuge.conf
   with open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r') as file:
      conf = file.readlines()
      
	   #Relay Template Variables
   return render_to_response("mod.ext", {
	   "conf"         :   str(conf[20]).rstrip('\n'),
	   "module_name"  :   request.META['PATH_INFO'].rstrip('/').strip('/'),
	   "module_page"  :   "mods/" + request.META['PATH_INFO'].rstrip('/').strip('/') + "_page.mod"
   })      
      
           
      #################################
      #HTTP CODE INJECTION MOD
      #################################

def httpcodeinjection(request, conf):
   # HTTP CODE INJECTION MODULE CONFIGURATION 
   exploit = ""
   payload = ""
   ip = ""
   port = "8080"


   # Status
   status = request.POST["status"]

   # Exploit
   if request.POST["iexploit"]:
      exploit = request.POST["iexploit"]

   # Payload
   if request.POST["payload"]:
      payload = request.POST["payload"]


   # Options
   # Custom Inject      
   if request.POST["custominject"]:
      exploit = "custom"
         # Write Custom Inject into File
      with open(str(os.path.dirname(__file__)) + '/httpcodeinjection/inject.x', 'w') as file:
         file.writelines(request.POST["custominject"])

   # Determine Metasploit Usage
   if request.POST["startmsf"]:
      msf = request.POST["startmsf"] + "\n"

   # Check IP/PORT
   if request.POST["injectip"]:
      ip = request.POST["injectip"]
   if request.POST["injectport"]:
      port = request.POST["injectport"]
       
   # Update Inject Status  
   installed.objects.filter(name = "httpcodeinjection").update(active = status)
   
   # Execute
   os.system('python ' + str(os.path.dirname(os.path.abspath(__file__))) + '/httpcodeinjection/httpcodeinjection.py ' + exploit + ' ' + payload + " " + ip + " " + port) 

   # Execute
   #os.system('xterm -e sh -c "python ' + str(os.path.dirname(os.path.abspath(__file__))) + '/httpcodeinjection/httpcodeinjection.py ' + method + ' ' + payload + '" &') 
  
   
      #################################
      #TUNNEL BLOCK MODULE
      #################################

def tunnelblock():
	os.system('python ' + str(os.path.dirname(os.path.abspath(__file__))) + '/TunnelBlock/TunnelBlock.py')


      #################################
      #WPAD Hijacking
      #################################
      
def wpad(request): 
	   # Read in subterfuge.conf
   with open(str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + 'subterfuge.conf', 'r') as file:
      conf = file.readlines()
      
	   #Relay Template Variables
   return render_to_response("wpad.dat", {
	   "na"  :   "na"
   })  
