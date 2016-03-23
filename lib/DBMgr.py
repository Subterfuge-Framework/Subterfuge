import sys
import os
import sqlite3

sys.path.append("../")

class dbmgr:
   def __init__( self):
      self.conn = sqlite3.connect('../attack.db', timeout=1) #You like the dick, you stupid variable python path piece of crap... !
      self.conn.execute('pragma foreign_keys = on')
      self.conn.commit()
      self.cur = self.conn.cursor()

   def getHosts(self):
      query = self.cur.execute("SELECT id, host, context, description, status from Hosts")
      return query

   def newHost(self, host, context, description, status):
      self.cur.execute("insert into Hosts (host, context, description, status) values ('" + host + "','" + context + "','" + description + "','" + status + "')")
      self.conn.commit()
      self.conn.close()

   def getChannels(self):
      query = self.cur.execute("SELECT id, HostID, Details, Tags from Channels")
      return query

   def getHostChannels(self):
      query = self.cur.execute("SELECT Channels.ID, HostID FROM Channels INNER JOIN Hosts ON Channels.HostID = Hosts.ID")
      return query

   def newChannel(self, hostid, details, tags):
      self.cur.execute("insert into Channels (HostID, Details, Tags) values ('" + hostid + "','" + details + "','" + tags + "')")
      self.conn.commit()
      self.conn.close()

   def getInteractions(self, channelid):
      query = self.cur.execute("SELECT ID, command FROM Interactions WHERE channelid =" + channelid + " AND status = 0")
      return query

   def newInteraction(self, hostid, channelid, command, response, status):
      self.cur.execute("insert into Interactions (hostid, channelid, command, response, status) values ('" + hostid + "','" + channelid + "','" + command + "','" + response + "','" + status + "')")
      self.conn.commit()
      self.conn.close()

   def closeInteraction(self, ID):
      self.cur.execute("update Interactions SET status='1' WHERE ID='" + ID + "'")
      self.conn.commit()
      self.conn.close()

   def LogCmdResponse(self, interactionid, response):
      #Update query
      self.cur.execute("insert into Interactions (hostid, channelid, command, response, status) values (" + hostid + "," + channelid + "," + command + "," + response + "," + status + ")")
      self.conn.commit()
      self.conn.close()

   def kill(self):
      self.conn.close()

   def __del__(self):
      #self.conn.close()
      pass
