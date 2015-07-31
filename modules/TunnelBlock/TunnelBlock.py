#!/usr/bin/python
import os

#SSH Tunnels
os.system("iptables -A FORWARD -p tcp --destination-port 22 -j DROP")
#PPTP Tunnels
os.system("iptables -A FORWARD -p tcp --destination-port 1723 -j DROP")
#L2TP Tunnels
os.system("iptables -A FORWARD -p udp --destination-port 500 -j DROP")
os.system("iptables -A FORWARD -p udp --destination-port 4500 -j DROP")
#Cisco IPSec Tunnels
os.system("iptables -A FORWARD -p udp --destination-port 10000 -j DROP")
#OpenVPN Tunnels
os.system("iptables -A FORWARD -p udp --destination-port 1194 -j DROP")
