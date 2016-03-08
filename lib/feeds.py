class rawPacket:
   def __init__(self):
      import scapy
      import os
      os.system('sysctl -w net.ipv4.ip_forward=1')

   def portProxy(self, FEED_PORT, PROXY_PORT):
      import os
      os.system('iptables -t nat -A PREROUTING -p tcp --destination-port ' + str(FEED_PORT) + ' -j REDIRECT --to-port ' + str(PROXY_PORT))
         
   def iptablesconfig(self, proxymode):
      os.system('iptables -F')
      os.system('iptables -X')
      os.system('iptables -t nat -F')
      os.system('iptables -t nat -X')
      os.system('iptables -t mangle -F')
      os.system('iptables -t mangle -X')
      os.system('iptables -P INPUT ACCEPT')
      os.system('iptables -P FORWARD ACCEPT')
      os.system('iptables -P OUTPUT ACCEPT')
      time.sleep(1)
      #10000 = SSLStrip & 10001 = MITMPROXY
      if proxymode == "sslstrip":
       os.system('iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port ' + PORT)
      elif proxymode == "mitmproxy":
       os.system('iptables -t nat -A PREROUTING -p tcp --destination-port 443 -j REDIRECT --to-port 10001')
       os.system('iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10001')

      time.sleep(1)
      print "Iptables Prerouting Configured\n"

      print 'Configuring System...'
      os.system('sysctl -w net.ipv4.ip_forward=1')
      print "IP Forwarding Enabled."