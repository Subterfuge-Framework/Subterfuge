import os

print "Remove and Rebuild db by executing: python manage.py syncdb"
raw_input("Press Enter when finished to continue")
print "Building Setting up Database..."
os.system("cat /usr/share/subterfuge/utilities/dev/build_db.sql | sqlite3 /usr/share/subterfuge/db")
os.system("rm /usr/share/subterfuge/base_db")
os.system("cp /usr/share/subterfuge/db /usr/share/subterfuge/base_db")

