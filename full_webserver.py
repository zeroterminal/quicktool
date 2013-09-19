#!/usr/bin/python

## Web Server #####
###################

import time
import os 

#############
## Intro ####

print ""
print ""
print "########################################"
print "## Web Server Installer By Zero         "
print "########################################"
print "##  ABOUT THE AUTHOR                  ##"
print "##  ___________________________       ##"
print "##  Name       : Jay                  ##"
print "##  mail       : zerolinuxx@gmail.com ##"
print "##  ubuntuone  : zerolinuxx@gmail.com ##"
print "##  facebook   : Itachi Sama          ##"
print "##  website    : coming soon          ##"
print "##                                    ##"
print "########################################"
print ""
print ""


print "*** This will install the web server"
web = raw_input( "Proceed? [Y/n]  ? ")

if( web == "y") or (web == "Y") or (web == ""):

	os.system("sudo apt-get install apache2")
	print ""
	phpgo = raw_input("*** Press enter when installation complete.")
	print ""
else:
	print "*** Program Terminated."
	print "."
	print ".."
	print "..."
	print "...."
	print ""
	print ""
	exit()

print ""
print "*** Now Installing php..."
print "."
print ".."
print "..."
print "...."
print ""
print ""
		
os.system("sudo apt-get install php5 libapache2-mod-php5 php5-cli php5-cgi php5-mysql ")
mysqlgo = raw_input("*** Press enter when installion is complete.")

print ""
print "*** Now Installing MySQL Database..."
print "."
print ".."
print "..."
print "...."
print ""
print ""
os.system("sudo apt-get install mysql-client mysql-common mysql-server phpmyadmin")

print "."
print ".."
print "..."
print "...."
print ""
print ""
		
phpgo = raw_input("*** Press enter when installation complete.")
time.sleep(1)

print "."
print ".."
print "..."
print "...."
print ""
print ""

## Start Web Server
start = raw_input("*** start webserver? [Y/n] ")
if (start != "y")  or (start != "Y") or (start != ""):
	print "."
	print ".."
	print "..."
	print "...."
	print ""
	print ""
	
	print "*** Installation Completed."
	print "*** Program Will Terminate in 3 Seconds"
	print "."
	print ".."
	print "..."
	print "...."
	print ""
	print ""

	print "*** Thank you for using Zero Webserver Installer."
	time.sleep(2)
	exit()
else:
	os.system("sudo /etc/init.d/apache2 start")
	print ""
	print ""
	print ""
	print ""
	print "*** Congratulations you have a Websever"
	print "*** Running to access it go to you favorite browser"
	print "*** and use http://localhost or http://127.0.0.1 as website"
	print "..."
	print ""
	print ""
	print ""
	print ""

	time.sleep(1)
	exit()
