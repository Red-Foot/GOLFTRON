#!usr/bin/python
#This is the world generator used by the program. It creates the world at random and then makes a map for the player.
from random import *
import math
from PIL import Image
import time

#set colors for map output
DwaterC = (0, 25, 103)
fairwayC = (56, 157, 39)
roughC = (0, 60, 12)
bunkerC= (238, 230, 126)
townC= (255, 255, 255)
dungeonC= (0, 0, 0)

#creates file for putting the arrays into
worldFile = open("worldtypes", "w+")

#sets map size
world = range(1,81)
worldFile.write("81\n")
#water gen, randomly generates 0 - 10 tiles---------------------------------------------------------------------------
totalDW = uniform(0,10)
#this if/else rounds the probably decimal uniform number to an integer
if (((totalDW+1)-totalDW) > 0.5):
	rtotDW = math.floor(totalDW)
else:
	rtotDW = math.ceil(totalDW)
worldDW = []
i = 0
while i <= rtotDW:
	w = choice(world)
	if ((w in worldDW) or (w == 1)):
		print(w)
		print("tile already occupied. retrying...")
	else:	
		print(w)
		print("tile unoccupied")
		worldDW.append(w)
		i += 1
print("DW")
print(worldDW)

#bunker gen, randomly generates 9-15 tiles----------------------------------------------------------------------------
worldB = []
totalB = uniform(9,15)
#this if/else rounds the probably decimal uniform number to an integer
if (((totalB+1)-totalB) > 0.5):
	rtotB = math.floor(totalB)
else:
	rtotB = math.ceil(totalB)
i = 0
while i <= rtotB:
	x = choice(world)
	if ((x in worldDW) or (x == 1)):
		print(x)
		print("tile already occupied. retrying...")
	elif (x in (worldB)):
		print(x)
		print("tile already occupied. retrying...")
	else:
		print(x)
		print("tile unoccupied")
		worldB.append(x)
		i +=1
print("B")
print(worldB)

#rough gen, randomly generates 20-50 tiles----------------------------------------------------------------------------
worldR = []
totalR = uniform(20,50)
#this if/else rounds the probably decimal uniform number to an integer
if (((totalR+1)-totalR) > 0.5):
	rtotR = math.floor(totalR)
else:
	rtotR = math.ceil(totalR)
i=0
while i <= rtotR:
	y = choice(world)
	if ((y in worldDW) or (y in worldB) or (y == 1)):
		print(y)
		print("tile already occupied. retrying...")
	elif (y in (worldR)):
		print(y)
		print("tile already occupied. retrying...")
	else:
		print(y)
		print("tile unoccupied")
		worldR.append(y)
		i+=1
print("R")
print(worldR)

#fairwaygen, fills in the rest of the world with fairway tiles--------------------------------------------------------
worldF = []
totalF = 81-((len(worldR))+(len(worldB))+(len(worldDW)))
i=1
while i < totalF:
	z = choice(world)
	if ((z in worldDW) or (z in worldB) or (z in worldR)):
		print(z)
		print("tile already occupied. retrying...")
	elif (z in (worldF)):
		print(z)
		print("tile already occupied. retrying...")
	else:
		print(z)
		print("tile unoccupied")
		worldF.append(z)
		i+=1
	
print("F")
print(worldF)
worldDW.append(81)


#town gen, places two towns on the map on fairway tiles, turning them into town tiles---------------------------------
worldT = []
totalT = 2
i=0
while i < totalT:
	u = choice(world)
	if (u == 1):
		print("Tile not suitable for town. retrying...")
	
	elif (u in worldF):
		worldT.append(u)
		worldF.remove(u)
		i += 1
	else:
		print("Tile not suitable for town. retrying...")
print("T")
print(worldT)
#dungeon gen, places two dungeons on the map on non-fairway and non-water tiles, turning them into dungeon tiles------
worldD = []
totalD = 2
i=0
while i < totalD:
	t = choice(world)
	if (t in worldF):
		print("Tile not suitable for dungeon. retrying...")
	elif (t in worldDW):
		print("Tile not suitable for dungeon. retrying...")
	elif (t in worldB):
		worldD.append(t)
		worldB.remove(t)
		i += 1
	elif (t in worldR):
		worldD.append(t)
		worldR.remove(t)
		i +=1
	else:
		print("unexpected tiletype. retrying...")

#putting it all together, appends all the tilesets into one big list (for debugging only)-----------------------------
listAll = (worldF + worldR + worldB + worldDW + worldT + worldD)
listAll.sort()
print("together")
print(listAll)
print(len(listAll))


#making the color list for image gen, replaces the numerically ordered tiles with the map output colors---------------
worldColors = []
for v in listAll:
	if v in worldF:
		worldColors.append(fairwayC)
	elif v in worldR:
		worldColors.append(roughC)
	elif v in worldB:
		worldColors.append(bunkerC)
	elif v in worldDW:
		worldColors.append(DwaterC)
	elif v in worldT:
		worldColors.append(townC)
	elif v in worldD:
		worldColors.append(dungeonC)

print("World Colors")
print(worldColors)

#generating image-----------------------------------------------------------------------------------------------------
img = Image.new('RGB', (9,9))
img.putdata(worldColors)
img = img.resize((450,450))
img.save('worldmap.png')

#writing the world to a text file so the parser can read it later-----------------------------------------------------
worldDW.append("end")
worldR.append("end")
worldB.append("end")
worldF.append("end")
worldT.append("end")
worldD.append("end")
worldDW.insert(0, "end")
worldR.insert(0, "end")
worldB.insert(0, "end")
worldF.insert(0, "end")
worldT.insert(0, "end")
worldD.insert(0, "end")
listFile = ["water", worldDW, "rough", worldR, "bunker", worldB, "fairway", worldF, "town", worldT, "dungeon", worldD]
for x in listFile:
	worldFile.write(str(x))
	worldFile.write("\n")



