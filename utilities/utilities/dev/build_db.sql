--Main Database Models
INSERT INTO main_setup VALUES ("1", "", "", "", "yes", "3", "6", "8", "no", "", "yes", "sslstrip");


--Installed Modules
INSERT INTO modules_installed VALUES ("1", "httpcodeinjection", "no");
INSERT INTO modules_installed VALUES ("2", "tunnelblock", "no");
INSERT INTO modules_installed VALUES ("3", "dos", "no");
INSERT INTO modules_installed VALUES ("4", "harvester", "yes");

--Installed Vectors
INSERT INTO modules_vectors VALUES ("1", "ARP Cache Poisoning", "yes");
INSERT INTO modules_vectors VALUES ("2", "Wireless AP Generator", "no");
INSERT INTO modules_vectors VALUES ("3", "WPAD Hijacking", "no");
INSERT INTO modules_vectors VALUES ("4", "Rogue DHCP", "no");

--ARP Poison Instantiated
INSERT INTO modules_arppoison VALUES ("1", "", "");
