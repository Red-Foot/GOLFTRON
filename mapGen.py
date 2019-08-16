#!usr/bin/python
#This is the world generator used by the program. It creates the world at random and then makes a map for the player.
from random import *
import math
from PIL import Image
from multiprocessing import Process,Pipe
import time
import dng
import tng

class worldgen():
	#opens file for putting the arrays into
	worldFile = open("./output files/worldtypes", "a+")
	worldFile.seek(0)
	world = range(1,81)
	wate = []
	bunk = []
	roug = []
	fair = []
	town = []
	dung = []
	townName = []
	dungName = []
	def fullgen(sender):
		worldgen.wate = worldgen.watgen()
		worldgen.bunk = worldgen.bungen()
		worldgen.roug = worldgen.rougen()
		worldgen.fair = worldgen.faigen()
		worldgen.town = worldgen.towgen()
		worldgen.dung = worldgen.dungen()
		worldgen.townName = worldgen.tnamegen()
		worldgen.dungName = worldgen.dnamegen()
		worldgen.mapgen()
		for i in worldgen.fair:
			if i in worldgen.town:
				worldgen.fair.remove(i)
		for i in worldgen.roug:
			if i in worldgen.dung:
				worldgen.roug.remove(i)
		for i in worldgen.bunk:
			if i in worldgen.dung:
				worldgen.bunk.remove(i)
		sender.send(worldgen.wate)	
		sender.send(worldgen.bunk)
		sender.send(worldgen.roug)
		sender.send(worldgen.fair)
		sender.send(worldgen.town)
		sender.send(worldgen.dung)
		sender.send(worldgen.townName)
		sender.send(worldgen.dungName)
		sender.close()
		with open("./output files/savedworld", "a+") as sW:
			sW.write("a;")
			for i in worldgen.wate:
				sW.write(str(i))
				sW.write(';')
			sW.write("b;")
			for i in worldgen.bunk:
				sW.write(str(i))
				sW.write(';')
			sW.write("c;")
			for i in worldgen.roug:
				sW.write(str(i))
				sW.write(';')
			sW.write("d;")
			for i in worldgen.fair:
				sW.write(str(i))
				sW.write(';')
			sW.write("e;")
			for i in worldgen.town:
				sW.write(str(i))
				sW.write(';')
			sW.write("f;")
			for i in worldgen.dung:
				sW.write(str(i))
				sW.write(';')
			sW.write("g;")
			for i in worldgen.townName:
				sW.write(i)
				sW.write(';')
			sW.write("h;")
			for i in worldgen.dungName:
				sW.write(i)
				sW.write(';')
#water gen, randomly generates 1 - 11 tiles---------------------------------------------------------------------------
	def watgen():
		worldDW = []
		if ('water' in worldgen.worldFile.read()):
			print("already generated water.")
		worldgen.worldFile.seek(0)
		if ('water' not in worldgen.worldFile.read()):
			totalDW = uniform(0,10)
			#this if/else rounds the probably decimal uniform number to an integer
			if (((totalDW+1)-totalDW) > 0.5):
				rtotDW = math.floor(totalDW)
			else:
				rtotDW = math.ceil(totalDW)
			i = 0
			while i <= rtotDW:
				w = choice(worldgen.world)
				if ((w in worldDW) or (w == 1)):
					print(w)
					print("tile already occupied. retrying...")
				else:	
					print(w)
					print("tile unoccupied")
					worldDW.append(w)
					i += 1
			worldgen.worldFile.seek(2)
			worldgen.worldFile.write("water")
			if (81 not in worldDW):
				worldDW.append(81)
			print("DW")
			print(worldDW)
		return worldDW
#bunker gen, randomly generates 9-15 tiles----------------------------------------------------------------------------
	def bungen():
		worldDW = worldgen.wate
		worldB = []
		worldgen.worldFile.seek(0)
		if ('bunker' in worldgen.worldFile.read()):
			print("already generated bunkers.")
		worldgen.worldFile.seek(0)
		if ('bunker' not in worldgen.worldFile.read()):
			totalB = uniform(9,15)
			#this if/else rounds the probably decimal uniform number to an integer
			if (((totalB+1)-totalB) > 0.5):
				rtotB = math.floor(totalB)
			else:
				rtotB = math.ceil(totalB)
			i = 0
			while i <= rtotB:
				x = choice(worldgen.world)
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
			worldgen.worldFile.seek(2)
			worldgen.worldFile.write("bunker")
			print("B")
			print(worldB)
		return worldB
#rough gen, randomly generates 20-50 tiles----------------------------------------------------------------------------
	def rougen():	
		worldR = []
		worldDW = worldgen.wate
		worldB = worldgen.bunk
		print(worldB)
		print(worldDW)
		worldgen.worldFile.seek(0)
		if ('rough' in worldgen.worldFile.read()):
			print("already generated roughs.")
		worldgen.worldFile.seek(0)
		if ('rough' not in worldgen.worldFile.read()):
			totalR = uniform(20,50)
	#this if/else rounds the probably decimal uniform number to an integer
			if (((totalR+1)-totalR) > 0.5):
				rtotR = math.floor(totalR)
			else:
				rtotR = math.ceil(totalR)
			i=0
			while i <= rtotR:
				y = choice(worldgen.world)
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
			worldgen.worldFile.seek(2)
			worldgen.worldFile.write("rough")
			print("R")
			print(worldR)
		return worldR
#fairwaygen, fills in the rest of the world with fairway tiles--------------------------------------------------------
	def faigen():
		worldF = []
		worldDW = worldgen.wate
		worldB = worldgen.bunk
		worldR = worldgen.roug
		print(worldB)
		print(worldDW)
		print(worldR)
		worldgen.worldFile.seek(0)
		if ('fairway' in worldgen.worldFile.read()):
			print("already generated fairways.")
		worldgen.worldFile.seek(0)
		if ('fairway' not in worldgen.worldFile.read()):
			totalF = 81-((len(worldR))+(len(worldB))+(len(worldDW)))
			i=1
			while i < totalF:
				z = choice(worldgen.world)
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
			worldgen.worldFile.seek(2)
			worldgen.worldFile.write("fairway")
			print("F")
			print(worldF)
		return worldF
#town gen, places two towns on the map on fairway tiles, turning them into town tiles---------------------------------
	def towgen():
		worldT = []
		worldDW = worldgen.wate
		worldB = worldgen.bunk
		worldR = worldgen.roug
		worldF = worldgen.fair
		print(worldF)
		print(worldB)
		print(worldDW)
		print(worldR)
		#var = input("stopping for a second...")
		worldgen.worldFile.seek(0)
		if ('town' in worldgen.worldFile.read()):
			print("already generated towns.")
		worldgen.worldFile.seek(0)
		if ('town' not in worldgen.worldFile.read()):
			totalT = 2
			i=0
			while i < totalT:
				u = choice(worldgen.world)
				if (u == 1):
					print("Tile not suitable for town. retrying...")
					print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
				elif (u in worldF):
					worldT.append(u)
					worldF.remove(u)
					i += 1
				else:
					print(u)
					print("Tile not suitable for town. retrying...")
			worldgen.worldFile.seek(2)
			worldgen.worldFile.write("town")
			print("T")
			print(worldT)
		return worldT
#town name gen, generates names for the towns-------------------------------------------------------------------------
	def tnamegen():
		nameT = []
		worldgen.worldFile.seek(0)
		if ('tname' in worldgen.worldFile.read()):
			print("already generated town names.")
		worldgen.worldFile.seek(0)
		if ('tname' not in worldgen.worldFile.read()):
			totalTN = 2
			i=0
			while i < totalTN:
				TNa = tng.generator()
				nameT.append(TNa)
				i += 1
			worldgen.worldFile.seek(2)
			worldgen.worldFile.write("tname")
		return nameT
#dungeon gen, places two dungeons on the map on non-fairway and non-water tiles, turning them into dungeon tiles------
	def dungen():
		worldD = []
		worldDW = worldgen.wate
		worldB = worldgen.bunk
		worldR = worldgen.roug
		worldF = worldgen.fair
		worldgen.worldFile.seek(0)
		if ('dungeon' in worldgen.worldFile.read()):
			print("already generated dungeons.")
		worldgen.worldFile.seek(0)
		if ('dungeon' not in worldgen.worldFile.read()):
			totalD = 2
			i=0
			while i < totalD:
				t = choice(worldgen.world)
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
			worldgen.worldFile.seek(2)
			worldgen.worldFile.write("dungeon")
		return worldD
#dungeon name gen, generates names for the towns----------------------------------------------------------------------
	def dnamegen():
		nameD = []
		worldgen.worldFile.seek(0)
		if ('dname' in worldgen.worldFile.read()):
			print("already generated dungeon names.")
		worldgen.worldFile.seek(0)
		if ('dname' not in worldgen.worldFile.read()):
			totalDN = 2
			i=0
			while i < totalDN:
				DNa = dng.generator()
				nameD.append(DNa)
				i += 1
			worldgen.worldFile.seek(2)
			worldgen.worldFile.write("dname")
		return nameD
#generates map image using RGB tuples and a numerical list of the lists-----------------------------------------------
	def mapgen():
		listAll = (worldgen.wate + worldgen.bunk + worldgen.roug + worldgen.fair + worldgen.town + worldgen.dung)
		listAll.sort()
		DwaterC = (0, 25, 103)
		fairwayC = (56, 157, 39)
		roughC = (0, 60, 12)
		bunkerC= (238, 230, 126)
		townC= (255, 255, 255)
		dungeonC= (0, 0, 0)
		print(listAll)
		worldColors = []
		for v in listAll:
			if v in worldgen.fair:
				worldColors.append(fairwayC)
			elif v in worldgen.roug:
				worldColors.append(roughC)
			elif v in worldgen.bunk:
				worldColors.append(bunkerC)
			elif v in worldgen.wate:
				worldColors.append(DwaterC)
			elif v in worldgen.town:
				worldColors.append(townC)
			elif v in worldgen.dung:
				worldColors.append(dungeonC)
		print("World Colors")
		print(worldColors)
		#set colors for map output
		img = Image.new('RGB', (9,9))
		img.putdata(worldColors)
		img = img.resize((450,450))
		img.save('worldmap.png')
