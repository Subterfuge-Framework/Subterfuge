import sys
import os
import sqlite3

sys.path.append("../")

DATABASE = '/home/adhd/Desktop/projects/Subterfuge/attack.db'

class dbmgr:
   def __init__(self):
      self.conn = sqlite3.connect(DATABASE, timeout=1)
      self.conn.execute('pragma foreign_keys = on')
      self.conn.commit()
      self.cur = self.conn.cursor()
      
   def getJobs(self):
      #Get jobs from DB
      self.cur.execute("SELECT * FROM Jobs")
      return self.cur.fetchall()
   
   def enableJob(self, jid):
      #Set job status enabled
      self.cur.execute("UPDATE Jobs SET Enabled = 1 WHERE ID = " + str(jid))
      self.conn.commit()
      #self.conn.close()
      
   #Add source field to Loot table???
   def logLoot(self, details, datetime):
      #Set job status enabled
      HID = "0"
      new = "1"
      print "INSERT INTO Loot(HID, Details, Datetime, New) values ('" + HID + "','" + details + "','" + datetime + "','" + new + "')"
      self.cur.execute("INSERT INTO Loot(HID, Details, Datetime, New) values ('" + HID + "','" + details + "','" + datetime + "','" + new + "')") 
      self.conn.commit()
      #self.conn.close()

   def newChannel(self, hostid, details, tags):
      self.cur.execute("insert into Channels (HostID, Details, Tags) values ('" + hostid + "','" + details + "','" + tags + "')")
      self.conn.commit()
      self.conn.close()

   def getInteractions(self, channelid):
      query = self.cur.execute("SELECT ID, command FROM Interactions WHERE channelid =" + channelid + " AND status = 0")
      return query

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
