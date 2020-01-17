#!usr/bin/python
import sys
from pathlib import Path
import png
import mng
from mapGen import *
import linecache as lc
from multiprocessing import Process,Queue,Pipe
import itertools

#NEXT STEP: fit it to the style guide

# !! declaring global values !!
#words for travelling that the functions need to recognize
nord = ["North", "north", "N", "n"]
sud = ["South", "south", "S", "s"]
ost = ["East", "east", "E", "e"]
westen = ["West", "west", "W", "w"]
#the player's initial index numbers, can be modified by loading a save
PXN = 1		
TXN = 0
DXN = 0
# !! end declaring global values !!

#world generation
with open("./output files/worldtypes") as wF:
	FCt = wF.read()
	#create save data with the mapGen script
	if ("a" not in FCt):
		#intitalizes the lists we look through for PXN's tile type
		worldgen()
		if __name__ == '__main__':
			reciever, sender = Pipe(False)
			p = Process(target=worldgen.fullgen, args=(sender,))
			p.start()
			wat = reciever.recv()
			bun = reciever.recv()
			rou = reciever.recv()
			fai = reciever.recv()
			tow = reciever.recv()
			dun = reciever.recv()
			towN = reciever.recv()
			dunN = reciever.recv()
	else:
		#read from saved data
		with open("./output files/savedworld") as sD:
			sD.seek(0)
			strAll = sD.readline()
			listAll = strAll.split(";")
			wat = []
			bun = []
			rou = []
			fai = []
			tow = []
			dun = []
			towN = []
			dunN = []
			#converting raw data to a usable list
			for i in listAll:
				try:
					ni = int(i)
					ii = listAll.index(i)
					listAll.remove(i)
					listAll.insert(ii, ni)
				except ValueError:
					unusedIxnt = 3
			#splits the list into its component lists
			spl = [list(y) for x, y in itertools.groupby(listAll, 
 				   lambda z: z == 'a') if not x]
			wat, bun, rou, fai, tow, dun, towN, dunN = spl

#entry into towns/dungeons/etc.		
def enter(a):

	global PXN
	if (PXN in tow):				
		if (a == "town"):
			print("town entry")
			TXN = 1
		else:
			print("You cannot enter what is not here.")
	elif (PXN in dun):
		if (a == "dungeon"):
			print("dungeon entry")
			DXN = 1
		else:
			print("You cannot enter what is not here.")
	else: 
		print("You cannot enter what is not here.")

#a small function to store basic descriptions of area, used most with look
def looker(a):

	if (a in wat):
		loc = " a lake-sized body of water."
	elif (a in rou):
		loc = " a scraggly and untamed area of rough."
	elif (a in bun):
		loc = " a large divot filled with sand."
	elif (a in fai):
		loc = " a flat plain that would be perfect for golfing."
	elif (a in tow):
		tnumber = tow.index(a)
		tname = towN[tnumber]
		loc = (" a town. A sign nearby reads \"Welcome to " + tname + "\".")
	elif (a in dun):
		dnumber = dun.index(a)
		dname = dunN[dnumber]
		loc = (" a dungeon. It looks like " + dname + ".")
	else:
		loc = " an unearthly void filled with black fog."
	return (loc)

#describes your surroundings by comparing the lists of area types
def look(a):

	#look at where you are
	if (a == "here"):
		loc = looker(PXN)
		print("Your immediate surroundings are:" + loc)
	#look north
	elif (a in nord):
		loc = looker((PXN - 9))
		print("You see to the north:" + loc)
	#look south
	elif (a in sud):
		loc = looker((PXN + 9))
		print("You see to the south:" + loc)
	#look east
	elif (a in ost):
		loc = looker((PXN + 1))
		print("You see to the east:" + loc)
	#look west
	elif (a in westen):
		loc = looker((PXN - 1))
		print("You see to the west:" + loc)

def laugh():

	print("ha")

#the next four functions are for moving around
def north():

	global PXN
	if((PXN - 9) < 1):
		loc = looker((PXN - 9))
		print("There is no land to the north. Only" + loc)
	else:
		PXN -= 9
		print("You go to the north.")
		look("here")

def east():

	global PXN
	if((PXN + 1) > 81):
		loc = looker((PXN + 1))
		print("There is no land to the south. Only" + loc)
	else:
		PXN += 1
		print("You go to the east.")
		look("here")

def south():

	global PXN
	if((PXN + 9) > 81):
		loc = looker((PXN + 9))
		print("There is no land to the east. Only" + loc)
	else:
		PXN += 9
		print("You go to the south.")
		look("here")

def west():

	global PXN
	if((PXN - 1) < 1):
		loc = looker((PXN - 1))
		print("There is no land to the west. Only" + loc)
	else:
		PXN -= 1
		print("You go to the west.")
		look("here")

#test function, tells you the number of the tile you are currently on
def pxn():

	print(str(PXN))

#describes an item with just the input of the item's name
def desc(a):

	if (a == "a"):
		print("description here")

def quit():

	sys.exit()

def clean(a, b):
	i = 0
	while i < len(a):
		if a[i] in b:
			del a[i]
			i -= 1
		i += 1
	return a

while (True):
	ent = input("> ")
	entSp = ent.split(' ')
	args = {"look" : look, "enter": enter}
	noarg = {"ha" : laugh, "North" : north, "north" : north, "N" : north, 
			 "n" : north, "S" : south, "s" : south, "south" : south, 
			 "South" : south, "e" : east, "E" : east, "east" : east, 
			 "East" : east, "w" : west, "W" : west, "west" : west, 
			 "West" : west, "index" : pxn, "quit": quit}
	items = {"a"} 
	arguments = {"here"}
	destroy = {"the", "at", "my", "go", "to", "in"}
	entSp = clean(entSp, destroy)
	for c in entSp:
		if c in noarg:	
			#command is issued with no care for arguments	
			if c != "quit": #quit raises an error flag to cause the 
							#program to end, so it needs to be explicitly 								#made to bypass the try/catch
				try:
					noarg[c]()
					entSp.clear()
				except:
					print("I don't know how to " + c + ".")
				break
			else:
				noarg[c]()
		elif c in args:
			#command is issued using the word directly after the command as the 
			#argument
			try:
				args[c](entSp[1])
				entSp.clear()
			except:
				print(" What kind of " + c + "ing did you want to do? \
					  (specify further).")
			break
		
		elif c in (items):
			desc(entSp[0])
			entSp.clear()
		else:
			entSpJ = " ".join(entSp)
			print(entSpJ)
			print("I don't understand what you mean by \"" + c + "\".")
			x = len(entSp)
			break
