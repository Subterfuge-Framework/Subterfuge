CREATE TABLE Settings(
   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
   Host        VARCHAR(100)   NOT NULL,
   OS          VARCHAR(100),
   LastActive  VARCHAR(100)
);

CREATE TABLE Hosts(
   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
   Host        VARCHAR(100)   NOT NULL,
   OS          VARCHAR(100),
   LastActive  VARCHAR(100)
);

CREATE TABLE Loot(
   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
   HID         INTEGER   NOT NULL,
   Details     VARCHAR(100),
   Datetime    VARCHAR(100),
   New         INTEGER
);

CREATE TABLE Jobs(
   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
   Name        VARCHAR(100)   NOT NULL,
   Active      INTEGER,
   Enabled     INTEGER,
   CmdString   VARCHAR(100),
   Type        VARCHAR(100),
   PID         INTEGER
);

CREATE TABLE Feeds(
   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
   Type        VARCHAR(100)   NOT NULL,
   Name        VARCHAR(100)
);

CREATE TABLE Modules(
   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
   FID         INTEGER   NOT NULL,
   Name        VARCHAR(100),
   Active      INTEGER
);



insert into Hosts (host, os, lastactive)
VALUES ("172.16.15.36", "Windows", "15s");
insert into Hosts (host, os, lastactive)
VALUES ("172.16.15.245", "Linux", "52s");
insert into Hosts (host, os, lastactive)
VALUES ("172.16.15.23", "Windows", "2m 15s");


insert into Jobs (Name, Active, Enabled, CmdString, Type, PID)
VALUES ("HTTP Proxy", "1", "0", "rawPacket().portProxy(a);80,10000", "", "");
insert into Jobs (Name, Active, Enabled, CmdString, Type, PID)
VALUES ("SSLStrip", "1", "0", "sslstrip().proxy(a);10000", "", "");
insert into Jobs (Name, Active, Enabled, CmdString, Type, PID)
VALUES ("HTTP Credential Harvester", "1", "0", "harvester().httpHarvester(a);packages/sslstrip.log", "", "");
insert into Jobs (Name, Active, Enabled, CmdString, Type, PID)
VALUES ("Network-wide ARP Cache Poison", "1", "0", "arpPoison().poisonAll(a);10.0.0.1,8", "", "");

insert into Interactions (hostid, channelid, command, response, status)
VALUES ("1", "1", "notepad", "", "0");
insert into Interactions (hostid, channelid, command, response, status)
VALUES ("1", "1", "ls", "", "0");


