#!usr/bin/python
from random import *
import math
from PIL import Image
from multiprocessing import Process,Pipe
import time
import dng
import tng
import os, os.path


#generates towns
class towngen():
	townFileNum = 1
	townFileCheck = open("./output files/towndig", 'a+')
	if townFileNum in townFileCheck:
		print("there's a town with ID " + townFileNum + ". Retrying...")
		townFileNum += 1
	else:
		townFile = os.path.join(os.getcwd(), "town", str(townFileNum))
		print(townFile)
	townFile.seek(0)
	townsize = range(1,3)
	sizechoice = choice(towngen.townsize)
	if (sizechoice == 3):
		town = range(1,36)
	elif (sizechoice == 2):
		town = range(1,25)
	elif (sizechoice == 1):
		town = range(1,16)
	home = []
	stor = []
	inne = []
	path = []
	fiel = []
	storName = []
	inneName = []
	def fullgen(sender):
		towngen.home = towngen.homgen()
		towngen.stor = towngen.stogen()
		towngen.inne = towngen.inngen()
		towngen.cent = towngen.cengen()
		towngen.fiel = towngen.fiegen()
		towngen.storNname = towngen.snamegen()
		towngen.inneName = towngen.inamegen()
		sender.send(towngen.home)	
		sender.send(towngen.stor)
		sender.send(towngen.inne)
		sender.send(towngen.cent)
		sender.send(towngen.fiel)
		sender.send(towngen.storName)
		sender.send(towngen.inneName)
		sender.close()
		with open("./output files/savedtown", "a+") as sW:
			sW.write("a;")
			for i in towngen.home:
				sW.write(str(i))
				sW.write(';')
			sW.write("a;")
			for i in towngen.stor:
				sW.write(str(i))
				sW.write(';')
			sW.write("a;")
			for i in towngen.inne:
				sW.write(str(i))
				sW.write(';')
			sW.write("a;")
			for i in towngen.cent:
				sW.write(str(i))
				sW.write(';')
			sW.write("a;")
			for i in towngen.fiel:
				sW.write(str(i))
				sW.write(';')
			sW.write("a;")
			for i in towngen.storName:
				sW.write(str(i))
				sW.write(';')
			sW.write("a;")
			for i in towngen.inneName:
				sW.write(i)
				sW.write(';')
#home gen, randomly generates 2-6 tiles--------------------------------------------------------------------------------
	def homgen():
		townH = []
		if ('home' in towngen.townFile.read()):
			print("already generated homes.")
		towngen.townFile.seek(0)
		if ('home' not in towngen.townFile.read()):
			if (towngen.sizechoice == 3):
				totalH = uniform(4,6)
			elif (towngen.sizechoice == 2):
				totalH = uniform(3,5)
			else:
				totalH = uniform(2,4)
			#this if/else rounds the probably decimal uniform number to an integer
			if (((totalH+1)-totalH) > 0.5):
				rtotH = math.floor(totalH)
			else:
				rtotH = math.ceil(totalH)
			i = 0
			while i <= rtotH:
				w = choice(towngen.town)
				if w in townH:
					print(w)
					print("tile occupied. retrying...")
				else:
					print(w)
					print("tile unoccupied")
					townH.append(w)
				i += 1
			towngen.townFile.seek(2)
			towngen.townFile.write("home")
			print("H")
			print(townH)
		return townH
#store gen, randomly generates 0-4 tiles-------------------------------------------------------------------------------
	def stogen():
		townS = []
		townH = towngen.homgen()
		if ('store' in towngen.townFile.read()):
			print("already generated stores.")
		towngen.townFile.seek(0)
		if ('store' not in towngen.townFile.read()):
			if (towngen.sizechoice == 3):
				totalS = uniform(2,4)
			elif (towngen.sizechoice == 2):
				totalS = uniform(1,3)
			else:
				totalS = uniform(0,2)
			#this if/else rounds the probably decimal uniform number to an integer
			if (((totalS+1)-totalS) > 0.5):
				rtotS = math.floor(totalS)
			else:
				rtotS = math.ceil(totalS)
			i = 0
			while i <= rtotS:
				w = choice(towngen.town)
				if (w in townH):
					print(w)
					print("tile occupied. retrying...")
				elif (w in townS):
					print(w)
					print("tile occupied. retrying...")
				else:
					print(w)
					print("tile unoccupied")
					townS.append(w)
				i += 1
			towngen.townFile.seek(2)
			towngen.townFile.write("store")
			print("S")
			print(townS)
		return townS
#inn gen, randomly generates 0-3 tiles---------------------------------------------------------------------------------
	def inngen():
		townI = []
		townH = towngen.homgen()
		townS = towngen.stogen()
		if ('inn' in towngen.townFile.read()):
			print("already generated inns.")
		towngen.townFile.seek(0)
		if ('inn' not in towngen.townFile.read()):
			if (towngen.sizechoice == 3):
				totalI = uniform(2,3)
			elif (towngen.sizechoice == 2):
				totalI = uniform(1,2)
			else:
				totalI = uniform(0,1)
			#this if/else rounds the probably decimal uniform number to an integer
			if (((totalI+1)-totalI) > 0.5):
				rtotI = math.floor(totalI)
			else:
				rtotI = math.ceil(totalI)
			i = 0
			while i <= rtotI:
				w = choice(towngen.town)
				if (w in townH):
					print(w)
					print("tile occupied. retrying...")
				elif (w in townS):
					print(w)
					print("tile occupied. retrying...")
				elif (w in townI):
					print(w)
					print("tile occupied. retrying...")
				else:
					print(w)
					print("tile unoccupied")
					townI.append(w)
				i += 1
			towngen.townFile.seek(2)
			towngen.townFile.write("inn")
			print("I")
			print(townI)
		return townI
#town center gen, generates 0-3 town centers---------------------------------------------------------------------------
	def cengen():
		townC = []
		townH = towngen.homgen()
		townS = towngen.stogen()
		townI = towngen.inngen()
		if ('center' in towngen.townFile.read()):
			print("already generated centers.")
		towngen.townFile.seek(0)
		if ('center' not in towngen.townFile.read()):
			if (towngen.sizechoice == 3):
				totalC = uniform(1,3)
			elif (towngen.sizechoice == 2):
				totalC = uniform(1,2)
			else:
				totalC = uniform(0,1)
			#this if/else rounds the probably decimal uniform number to an integer
			if (((totalC+1)-totalC) > 0.5):
				rtotC = math.floor(totalC)
			else:
				rtotC = math.ceil(totalC)
			i = 0
			while i <= rtotC:
				w = choice(towngen.town)
				if (w in townH):
					print(w)
					print("tile occupied. retrying...")
				elif (w in townS):
					print(w)
					print("tile occupied. retrying...")
				elif (w in townI):
					print(w)
					print("tile occupied. retrying...")
				elif (w in townC):
					print(w)
					print("tile occupied. retrying...")
				else:
					print(w)
					print("tile unoccupied")
					townC.append(w)
				i += 1
			towngen.townFile.seek(2)
			towngen.townFile.write("center")
			print("C")
			print(townC)
		return townC
#field gen, places fields wherever the rest of the tiles are not-------------------------------------------------------
	def feigen():
		townF = []
		townH = towngen.homgen()
		townS = towngen.stogen()
		townI = towngen.inngen()
		townC = towngen.cengen()
		if ('field' in towngen.townFile.read()):
			print("already generated fields.")
		towngen.townFile.seek(0)
		if ('field' not in towngen.townFile.read()):
			if (towngen.sizechoice == 3):
				rtotF = 36 - (len(townH) + len(townS) + len(townI) + len(townC))
			elif (towngen.sizechoice == 2):
								rtotF = 25 - (len(townH) + len(townS) + len(townI) + len(townC))
			else:
				rtotF = 16 - (len(townH) + len(townS) + len(townI) + len(townC))
			i = 0
			while i <= rtotF:
				w = choice(towngen.town)
				if (w in townH):
					print(w)
					print("tile occupied. retrying...")
				elif (w in townS):
					print(w)
					print("tile occupied. retrying...")
				elif (w in townI):
					print(w)
					print("tile occupied. retrying...")
				elif (w in townC):
					print(w)
					print("tile occupied. retrying...")
				elif (w in townF):
					print(w)
					print("tile occupied. retrying...")
				else:
					print(w)
					print("tile unoccupied")
					townF.append(w)
				i += 1
			towngen.townFile.seek(2)
			towngen.townFile.write("field")
			print("F")
			print(townF)
		return townF
#store name gen, generates names for the stores------------------------------------------------------------------------
	def snamegen():
		nameS = []
		townS = towngen.stogen()
		towngen.townFile.seek(0)
		if ('sname' in towngen.townFile.read()):
			print("already generated store names.")
		worldgen.worldFile.seek(0)
		if ('sname' not in towngen.townFile.read()):
			totalSN = len(townS)
			i=0
			while i < totalSN:
				SNa = sng.generator()
				nameS.append(SNa)
				i += 1
			towngen.townFile.seek(2)
			towngen.townFile.write("sname")
		return nameS

#inn name gen, generates names for the inns----------------------------------------------------------------------------
	def inamegen():
		nameI = []
		townI = towngen.inngen()
		towngen.townFile.seek(0)
		if ('iname' in towngen.townFile.read()):
			print("already generated inn names.")
		worldgen.worldFile.seek(0)
		if ('iname' not in towngen.townFile.read()):
			totalIN = len(townI)
			i=0
			while i < totalIN:
				INa = sng.generator()
				nameI.append(INa)
				i += 1
			towngen.townFile.seek(2)
			towngen.townFile.write("iname")
		return nameI

