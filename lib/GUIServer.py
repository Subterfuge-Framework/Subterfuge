import BaseHTTPServer
import cgi
import configparser
import logging
import os
import SimpleHTTPServer
import SocketServer
import ssl
import sqlite3
import re

from subprocess import Popen, PIPE

CWD = os.getcwd()
ATTACKDB = os.path.join(CWD, "attack.db")
print ATTACKDB
from lib.dbmgr import *

PORT = 8080
print ""


# WEBDIR = "../gui/"

# Class to handle commands delivered by the GUI
class C2Handler:
    # def __init__( self, target):
    #   self.target = target

    def formHandler(self, form):
        cmd, channel = re.findall("'([^']+)'", str(form))


# Class to dynamically generate and deliver the interface to a browser
class guiBuilder:
    def __init__(self):
        import sys
        sys.path.append("../")

    def index(self):
        with open("gui/index.htm") as page:
            content = page.readlines()

        # hosts = dbmgr().getHosts()

        # htable = guiObjects().hostTable(hosts)

        # Get info from db
        nloot = "5"

        page_variables = ""

        new_loot = '<div id = "new_loot">' + nloot + '</div>'

        # page_variables += new_loot

        newlines = []
        #### Variable Parser
        for line in content:
            if "{{{" in line:
                r = re.compile('{{{(.*?)}}}')
                m = r.search(line)

                # print "Inserting page vars"

                newlines.append(line.replace("{{{}}}", page_variables))

            else:
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
            # else:


            site = ' '.join(newlines)

        return site


# Class to build specific interface objects
class guiObjects:
    def hostTable(self, hosts):
        table = ""
        i = 0
        for host in hosts:
            if (i % 2 == 0):
                trclass = '<tr class = "widgetrowa">'
            else:
                trclass = '<tr class = "widgetrowb">'

            row = trclass + '<td width = "30%">' + host[1] + '</td><td width = "30%">' + host[
                2] + '</td><td width = "30%">' + host[3] + '</td><td width = "30%">' + host[4] + '</td></tr>'
            table += row
            i = i + 1

        return table


# Class to dynamically generate and deliver the interface to a browser
# Convert to dbmgr
class dbHandler:
   def __init__(self):
      import sys
      sys.path.append("../")

   def dbquery(self, qstring):
      import base64
      import sqlite3
      import json

      string = base64.b64decode(qstring.split('qstring=')[1].split('&')[0])

      try:
         self.conn = sqlite3.connect(ATTACKDB,
                                    timeout=1)  # You like the dick, you stupid variable python path piece of crap... !
         self.conn.execute('pragma foreign_keys = on')
         self.conn.commit()
         self.cur = self.conn.cursor()
         query = self.cur.execute(string)
         
      except sqlite3.Error as e:
         print "Error:", e.message

      # Iterate through query results & append to list
      r = [dict((query.description[i][0], value) for i, value in enumerate(row)) for row in query.fetchall()]

      return json.dumps(r)
   
   def dbupdate(self, qstring):
      import base64
      import sqlite3
      import json
      
      string = base64.b64decode(qstring.split('qstring=')[1].split('&')[0])

      try:
         self.conn = sqlite3.connect(ATTACKDB,
                                    timeout=1)
         self.conn.execute('pragma foreign_keys = on')
         self.cur = self.conn.cursor()
         self.cur.execute(string)
         self.conn.commit()
         
      except sqlite3.Error as e:
         print "Error:", e.message
         

# Class to handle browser requests
class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def log_request(self, code='-', size='-'):
        pass

    def log_error(self, format, *args):
        pass

    def do_GET(self):
        if self.path == '/':
            # This URL will trigger our sample function and send what it returns back to the browser
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(guiBuilder().index())  # call sample function here
            return


        elif self.path.split('?')[0] == '/dbquery':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(dbHandler().dbquery(self.path.split('?')[1]))  # call sample
            return
         
        elif self.path.split('?')[0] == '/dbupdate':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(dbHandler().dbupdate(self.path.split('?')[1]))  # call sample
            return

        else:
            print self.path.split('?')[0]
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/start/':
            import os
            import subprocess

            subterfuge_dir = os.path.dirname(os.path.dirname(__file__))
            process = subprocess.Popen('python ' + subterfuge_dir + '/mitmserver.py &', shell=True)

            print "Executing MITM Exploitation Server!"

        elif self.path == '/config/':
            print "Making attack configuration adjustments..."

        elif self.path == '/newjob/':
            print "Configuring new attack job..."

            jobDict = {
                Name: "tmp",
                Active: "1",
                Enabled: "0",
                CmdString: "tmp",
                Type: "tmp",
                PID: "1000"
            }

            dbmgr().createJob(jobDict)


        else:
            print "POSTS"
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })
            # logging.warning("============= POST VALUES ==============")
            for item in form.list:
                logging.warning(item)
            logging.warning("\n")
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
            C2Handler().formHandler(form.list)
