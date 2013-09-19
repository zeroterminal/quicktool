#!/usr/bin/python

import time
import os 
import random

#############
## Intro ####

print ""
print ""
print "########################################"
print "## gnum By Zero                         "
print "########################################"
print "##  ABOUT THE AUTHOR                  ##"
print "##  ___________________________       ##"
print "##  Name       : Jay                  ##"
print "##  mail       : zerolinuxx@gmail.com ##"
print "##  ubuntuone  : zerolinuxx@gmail.com ##"
print "##  website    : coming soon          ##"
print "##                                    ##"
print "########################################"
print ""
print ""


## Coniguration #########
#########################

print "[] Guessing Game initiated "
print "[] select difficulty "
print ""
print ""
print "Level 1 : [ Example    *      ] "
print "Level 2 : [ Easy       **     ] "
print "Level 3 : [ Medium     ***    ] "
print "Level 4 : [ Hard       ****   ] "
print "Level 5 : [ Nightmare  *****  ] "
print ""
print ""
print "**********************"
print ""
print "Level 2 is made up of 2 numbers such as 10,    99"
print "Level 3 is made up of 3 numbers such as 100,   999"
print "Level 4 is made up of 4 numbers such as 1000,  9999"
print "Level 5 is made up of 5 numbers such as 10000, 99999"
print ""
print "**********************"
print ""
print ""
print "*** SCORE EQUATION IS : ( Tries x Level ) "
print "*** Good Luck & Enjoy!"
print ""
print "======================"
gamelevel = int(input("choose (level 1 2 3 4 5) : " ))
print ""
print "======================"
print "*** Proccessing... "
time.sleep(2)
print "*** Loading completed ..."
print ""
time.sleep(1)
print "###########################"
print "Game Initiated ..."
print "###########################"


## Set Diffuclty ########
#########################

if (gamelevel == None):
	print "Error! select a level"
	gamelevel = int(input("choose level 1 2 3 4 5"))
else:	
	if(gamelevel == 1):
		gnum = random.randint(0,9)
		tries=3
		print ""
		print "----- THIS IS FOR TRAINING :: SECRET ANSWER IS (",gnum,") ."
		print ""


	elif(gamelevel == 2):
		gnum = random.randint(0,99)
		tries=5


	elif(gamelevel == 3):
		gnum = random.randint(0,999)
		tries=7


	elif(gamelevel == 4):
		gnum = random.randint(0,9999)
		tries=12


	elif(gamelevel == 5):
		(gnum) = random.randint(0,99999)
		tries=18



## CHECK RESULTS ######
#######################


print ""
while(tries >=0):
	time.sleep(1)

	answer = input("       [ choose a number? ] : ")

	time.sleep(2)
	if(answer != gnum):
		print "",""
		print "========================================="
		print "====  BEEP! Wrong answer"
		print "====  Try again"
		print "========================================="
		print "",""
		if(answer > gnum):
			tries-=1
			print "","",""
			print "                    >>> YOUR NUMBER IS **** BIGGER **** REDUCE THE VALUE "
			print ""
			print ""
			print "#########################################"
			print "##           Tries left : ",tries
			print "#########################################"
			print "_________________________________________"
			print "","",""
		if(answer < gnum):
			tries-=1
			print "","",""
			print "                    >>> YOUR NUMBER IS **** SMALLER **** INCREASE THE VALUE "
			print ""
			print ""
			print "#########################################"
			print "##           Tries left : ",tries
			print "#########################################"
			print "_________________________________________"
			print "","",""
		if(tries == 0):
			print ""
			print " WRONG ANSWER !"
			print " GAME OVER !"
			print " BETTER LUCK NEXT TIME !"
			print " ANSWER WAS ",gnum 
			break
	elif(answer == gnum):
		print "","",""
		print "YOUR SCORE IS  ################ (", tries*gamelevel,")################"
		print ""
		print "================================================================================="
		print "                                                                                 "
		print "!!!!!!!!!!!!!!!**************    CONGRATULATIONS    **************!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!************** THANK YOU FOR PLAYING **************!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!**************   WATCH CODE GEASS!   **************!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!******* _FORMAT YOUR WINDOWS INSTALL UBUNTU_ ******!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!**************   ALL HAIL LINUX !    **************!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!**************   ALL HAIL LINUX !    **************!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!**************   ALL HAIL LINUX !    **************!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!**************   ALL HAIL LINUX !    **************!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!**************   ALL HAIL LINUX !    **************!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!**************   ALL HAIL LINUX !    **************!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!**************   ALL HAIL LINUX !    **************!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!**************   ALL HAIL LINUX !    **************!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!**************   ALL HAIL LINUX !    **************!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!**************   ALL HAIL LINUX !    **************!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!**************   ALL HAIL LINUX !    **************!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!**************   ALL HAIL LINUX !    **************!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!**************   ALL HAIL LINUX !    **************!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!**************   ALL HAIL LINUX !    **************!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!**************   ALL HAIL LINUX !    **************!!!!!!!!!!!!!!!"
		print "!!!!!!!!!!!!!!!**************   ALL HAIL LINUX !    **************!!!!!!!!!!!!!!!"
		print "================================================================================="
		print "","",""
		break
		
//End
