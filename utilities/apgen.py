#!/usr/bin/python
import os
import sys
import time

    #Read in Arguments
essid = sys.argv[1]
channel = 1
antenna_nic = sys.argv[2]
internet_nic = sys.argv[3]


os.system('killall -9 dhclient')
os.system('killall -9 dhclient3')

os.system('airmon-ng start ' + antenna_nic + ' ' + str(channel))
os.system('airbase-ng -e ' + essid + ' -c ' + str(channel) + ' mon0 &')
time.sleep(2)
os.system('airodump-ng -c ' + str(channel) + ' mon0 &')
time.sleep(2)
os.system('ifconfig at0 192.168.2.129 netmask 255.255.255.128')
os.system('route add -net 192.168.2.128 netmask 255.255.255.128 gw 192.168.2.129')
os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
os.system('iptables -F')
os.system('iptables -t nat -F')
os.system('iptables --delete-chain')
os.system('iptables -t nat --delete-chain')
os.system('iptables -t nat --append POSTROUTING -o ' + internet_nic + ' -j MASQUERADE')
os.system('iptables --append FORWARD --in-interface at0 -j ACCEPT')
time.sleep(2)
os.system('dhcpd3')
time.sleep(10)
