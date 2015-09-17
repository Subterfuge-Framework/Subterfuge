#!/usr/bin/python
import os
import sys
import time

os.system('killall -9 airbase-ng')
os.system('airmon-ng stop mon0')
os.system('airmon-ng stop at0')
os.system('ifconfig at0 down')
os.system('iptables -F')
os.system('iptables -t nat -F')
os.system('iptables --delete-chain')
os.system('iptables -t nat --delete-chain')
os.system('airmon-ng stop mon0')
os.system('airmon-ng stop at0')
os.system('killall -9 dhcpd3')
