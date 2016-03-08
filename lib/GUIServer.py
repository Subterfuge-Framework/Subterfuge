import BaseHTTPServer
import SimpleHTTPServer
import SocketServer
from subprocess import Popen, PIPE
import logging
import cgi
import ssl
import os
import re

import sqlite3


PORT = 8080
print ""
#WEBDIR = "../gui/"

#Class to handle commands delivered by the GUI
class C2Handler:
   #def __init__( self, target):
   #   self.target = target

   def formHandler(self, form):
      #if CMD
      #try:
         #print str(form).split(",")[0].split("'")[1]
         #print str(form).split(",")[2].split("'")[1]
         cmd = str(form).split(",")[3].split("'")[1]
         channel = str(form).split(",")[1].split("'")[1]
         #dbmgr().newInteraction("", channel, cmd, "", "0")
      #except:
         print form

	  
#Class to dynamically generate and deliver the interface to a browser
class guiBuilder:
   def __init__( self):
      import sys
      sys.path.append("../")

   def index(self):
      with open("gui/index.htm") as page:
         content = page.readlines()

      #hosts = dbmgr().getHosts()

      #htable = guiObjects().hostTable(hosts)
      
      newlines = []
      #### Variable Parser
      for line in content:
         if "{{{" in line:
            r = re.compile('{{{(.*?)}}}')
            m = r.search(line)
            
         newlines.append(line)
            
         '''
         #if variable name is x
            if m:
               print m.group(1)
               if m.group(1) == "hosts_table":
                  newlines.append(line.replace("{{{hosts_table}}}", htable))
                  #print newlines
                  #print "Building Table"
         '''
         #else:


         site = ' '.join(newlines)

      return site

#Class to build specific interface objects
class guiObjects:
   def hostTable(self, hosts):
      table = ""
      i = 0
      for host in hosts:
         if (i % 2 == 0):
            trclass = '<tr class = "widgetrowa">'
         else:
            trclass = '<tr class = "widgetrowb">'
        
         row = trclass + '<td width = "30%">' + host[1] + '</td><td width = "30%">' + host[2] + '</td><td width = "30%">' + host[3] + '</td><td width = "30%">' + host[4] + '</td></tr>'
         table += row
         i = i + 1

      return table


#Class to handle browser requests
class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
   def do_GET(self):
      #logging.warning("============= GET STARTED ==============")
      #logging.warning(self.headers)

      if self.path=='/':
         #This URL will trigger our sample function and send what it returns back to the browser
         self.send_response(200)
         self.send_header('Content-type','text/html')
         self.end_headers()
         self.wfile.write(guiBuilder().index()) #call sample function here
         return
      else:
         #print self.path
         SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

   def do_POST(self):
      logging.warning("============= POST STARTED =============")
      logging.warning(self.headers)
      form = cgi.FieldStorage(
         fp=self.rfile,
         headers=self.headers,
         environ={'REQUEST_METHOD':'POST',
                  'CONTENT_TYPE': self.headers['Content-Type'],
                 })
      logging.warning("============= POST VALUES ==============")
      for item in form.list:
         logging.warning(item)
      logging.warning("\n")
      SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
      C2Handler().formHandler(form.list)



