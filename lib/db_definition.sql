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
   New         VARCHAR(100)
);

CREATE TABLE Jobs(
   ID INTEGER PRIMARY KEY   AUTOINCREMENT,
   Name        VARCHAR(100)   NOT NULL,
   Active      INTEGER
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

insert into Loot (HID, Details, Datetime, New)
VALUES ("1", "http - yahoo.com; username: subterfuge@gmail.com; password: omgbdaycake", "03/27/91", "0");
insert into Loot (HID, Details, Datetime, New)
VALUES ("3", "http cookie - twitter.com; sid=50af74a39d885e9d:T=1439480733:S=ALNI_MZlPFhvB2gai55AqitO6_1VckKoEA;", "03/27/91", "0");
insert into Loot (HID, Details, Datetime, New)
VALUES ("3", "ftp - 31.3.3.7; username: subterfuge@gmail.com; password: omgbdaycake", "03/24/16", "1");
insert into Loot (HID, Details, Datetime, New)
VALUES ("3", "NTLM - 
user::WORKGROUP:1122334455667788:6FAF764ECFDF1D1D9E7BA7B517190F3B:E15C1A679C7609CE", "03/24/16", "1");
insert into Loot (HID, Details, Datetime, New)
VALUES ("1", "http - ebay.com; username: subterfuge@gmail.com; password: omgbdaycake", "03/24/16", "1");
insert into Loot (HID, Details, Datetime, New)
VALUES ("2", "http - facebook.com; username: subterfuge@gmail.com; password: omgbdaycake", "03/24/16", "1");



insert into Interactions (hostid, channelid, command, response, status)
VALUES ("1", "1", "notepad", "", "0");
insert into Interactions (hostid, channelid, command, response, status)
VALUES ("1", "1", "ls", "", "0");