#!usr/bin/python
#haha yes
import tkinter as tk
from tkinter import Frame
from pathlib import Path
import png
import mng
from mapGen import *
import linecache as lc
from multiprocessing import Process,Queue,Pipe
import itertools

root = tk.Tk()
root.configure(background="black")
class App(tk.Tk):

	def __init__(self, master):
		#setting up the initial state of the game when you load in.
		master.minsize(802,400)
		master.maxsize(802,400)
		self.yv = 0
		self.twoyv = 0
		initS = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n>initialize\none two"
		self.disp = tk.StringVar()
		self.disp.set(initS)
		self.output = tk.Label(master, textvariable=self.disp, bg="black",wraplength=800, foreground="white",anchor="w",justify="left")
		self.output.grid(row=0,column=0,sticky="SW",rowspan=2,columnspan=3)
		self.entry = tk.Entry(master, bg="black", foreground="white",width=95)
		self.entry.grid(row=3, column=1,sticky="W")
		self.entry.place(x=15,y=380)
		self.label = tk.Label(master, text=">", bg="black", foreground="white")
		self.label.grid(row=3, column=0,sticky="W")
		self.label.place(x=1,y=380)
		#initializes the player's index number
		self.PXN = 1		
		#if the game has run before we choose not to regenerate it
		with open("./output files/worldtypes") as wF:
			FCt = wF.read()
			print(FCt)
			if ("a" not in FCt):
				print("this should only appear when the world is being populated for the first time.")
				#intitalizes the lists we look through for PXN's tile type
				worldgen()
				if __name__ == '__main__':
					reciever, sender = Pipe(False)
					p = Process(target=worldgen.fullgen, args=(sender,))
					p.start()
					self.wat = reciever.recv()
					self.bun = reciever.recv()
					self.rou = reciever.recv()
					self.fai = reciever.recv()
					self.tow = reciever.recv()
					self.dun = reciever.recv()
					self.towN = reciever.recv()
					self.dunN = reciever.recv()
			else:
				#read from saved data
				print("work now?")
				with open("./output files/savedworld") as sD:
					sD.seek(0)
					strAll = sD.readline()
					listAll = strAll.split(";")
					self.wat = []
					self.bun = []
					self.rou = []
					self.fai = []
					self.tow = []
					self.dun = []
					self.towN = []
					self.dunN = []
					#converting raw data to a usable format
					#water conversion
					for i in listAll:
						if i == "b":
							print("breaking")
							break
						elif i == "a":
							print("cont")
						else:
							print("appending " + i)
							self.wat.append(int(i))
					print("water")
					print(self.wat)
					del listAll[0]
					for i in self.wat:
						ii = str(i)
						if (ii in listAll):
							listAll.remove(ii)
					print(listAll)
					#bunker conversion
					for i in listAll:
						if i == "c":
							print("breaking")
							break
						elif i == "b":
							print("cont")
						else:
							print("appending " + i)
							self.bun.append(int(i))
					print("bunker")
					print(self.bun)
					del listAll[0]
					for i in self.bun:
						ii = str(i)
						if (ii in listAll):
							listAll.remove(ii)
					print(listAll)
					#rough conversion
					for i in listAll:
						if i == "d":
							print("breaking")
							break
						elif i == "c":
							print("cont")
						else:
							print("appending " + i)
							self.rou.append(int(i))
					print("rough")
					print(self.rou)
					del listAll[0]
					for i in self.rou:
						ii = str(i)
						if (ii in listAll):
							listAll.remove(ii)
					print(listAll)
					#fairway conversion
					for i in listAll:
						if i == "e":
							print("breaking")
							break
						elif i == "d":
							print("cont")
						else:
							print("appending " + i)
							self.fai.append(int(i))
					print("fairway")
					print(self.fai)
					del listAll[0]
					for i in self.fai:
						ii = str(i)
						if (ii in listAll):
							listAll.remove(ii)
					print(listAll)
					#town conversion
					for i in listAll:
						if i == "f":
							print("breaking")
							break
						elif i == "e":
							print("cont")
						else:
							print("appending " + i)
							self.tow.append(int(i))
					print("town")
					print(self.tow)
					del listAll[0]
					for i in self.tow:
						ii = str(i)
						if (ii in listAll):
							listAll.remove(ii)
					print(listAll)
					#dungeon conversion
					for i in listAll:
						if i == "g":
							print("breaking")
							break
						elif i == "f":
							print("cont")
						else:
							print("appending " + i)
							self.dun.append(int(i))
					print("dungeon")
					print(self.dun)
					del listAll[0]
					for i in self.dun:
						ii = str(i)
						if (ii in listAll):
							listAll.remove(ii)
					print(listAll)
					#town name conversion
					for i in listAll:
						if i == "h":
							print("breaking")
							break
						elif i == "g":
							print("cont")
						else:
							print("appending " + i)
							self.towN.append(i)
					print("town names")
					print(self.towN)
					del listAll[0]
					for i in self.towN:
						if (i in listAll):
							listAll.remove(i)
					print(listAll)
					#dungeon name conversion
					for i in listAll:
						if i == "":
							print("breaking")
							break
						elif i == "h":
							print("cont")
						else:
							print("appending " + i)
							self.dunN.append(i)
					print("dungeon names")
					print(self.dunN)
					del listAll[0]
					for i in self.dunN:
						
						if (i in listAll):
							listAll.remove(i)
					print(listAll)
		#lists of all possible spellings of directions, one per direction
		self.nord = ["North", "north", "N", "n"]
		self.sud = ["South", "south", "S", "s"]
		self.ost = ["East", "east", "E", "e"]
		self.westen = ["West", "west", "W", "w"]		
		print("37")
		root.bind('<Return>', self.onEnter)
	def onEnter(self,event):
		#declaring the variables defined above so they can be used
		ent = self.entry.get()
		self.yv -= 15
		self.PXN
		self.nord
		self.sud
		self.ost
		self.westen
		self.wat
		self.bun
		self.rou
		self.fai
		self.tow
		self.dun
		self.towN
		self.dunN
		def laugh():
			sha = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "ha")
			self.output['text'] = sha
			self.twoyv -= 30
		class ee:
			#test function
			def printer(a):
				stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + a)
				self.output['text'] = stes
				self.twoyv -= 30
			#describes your surroundings by comparing the lists of area types
			def look(a):
				#look at where you are
				if (a == "here"):
					if (self.PXN in self.wat):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You're in water.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif (self.PXN in self.rou):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You're in rough.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif (self.PXN in self.bun):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You're in bunker.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif (self.PXN in self.fai):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You're in fairway.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif (self.PXN in self.tow):
						tnumber = self.tow.index(self.PXN)
						tname = self.towN[tnumber]
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You approach a town. A sign reads \" Welcome to " + tname + "\".")
						self.output['text'] = stes
						self.twoyv -= 30
					elif (self.PXN in self.dun):
						dnumber = self.dun.index(self.PXN)
						dname = self.dunN[dnumber]
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You approach a dungeon. It looks like a " + dname + ".")
						self.output['text'] = stes
						self.twoyv -= 30
				#look north
				elif (a in self.nord):
					if ((self.PXN - 9) in self.wat):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see water.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((self.PXN - 9) in self.rou):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see rough.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((self.PXN - 9) in self.bun):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see bunker.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((self.PXN - 9) in self.fai):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see fairway.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((self.PXN - 9) in self.tow):
						tnumber = self.tow.index((self.PXN - 9))
						tname = self.towN[tnumber]
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a town, and can make out a distant sign. It reads: \n \" Welcome to " + tname + "\".")
						self.output['text'] = stes
						self.twoyv -= 45
					elif ((self.PXN - 9) in self.dun):
						dnumber = self.dun.index((self.PXN - 9))
						dname = self.dunN[dnumber]
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a dungeon. It looks like a " + dname + ".")
						self.output['text'] = stes
						self.twoyv -= 30
					else:
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "The only thing you see to the north is an endless evil fog.")
						self.output['text'] = stes
						self.twoyv -= 30
				#look south
				elif (a in self.sud):
					if ((self.PXN + 9) in self.wat):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see water.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((self.PXN + 9) in self.rou):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see rough.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((self.PXN + 9) in self.bun):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see bunker.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((self.PXN + 9) in self.fai):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see fairway.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((self.PXN + 9) in self.tow):
						tnumber = self.tow.index((self.PXN + 9))
						tname = self.towN[tnumber]
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a town, and can make out a distant sign. It reads: \n \" Welcome to " + tname + "\".")
						self.output['text'] = stes
						self.twoyv -= 45
					elif ((self.PXN + 9) in self.dun):
						dnumber = self.dun.index((self.PXN + 9))
						dname = self.dunN[dnumber]
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a dungeon. It looks like a " + dname + ".")
						self.output['text'] = stes
						self.twoyv -= 30
					else:
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "The only thing you see to the south is an endless evil fog.")
						self.output['text'] = stes
						self.twoyv -= 30
				#look east
				elif (a in self.ost):
					if ((self.PXN + 1) in self.wat):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see water.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((self.PXN + 1) in self.rou):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see rough.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((self.PXN + 1) in self.bun):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see bunker.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((self.PXN + 1) in self.fai):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see fairway.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((self.PXN + 1) in self.tow):
						tnumber = self.tow.index((self.PXN + 1))
						tname = self.towN[tnumber]
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a town, and can make out a distant sign. It reads: \n \" Welcome to " + tname + "\".")
						self.output['text'] = stes
						self.twoyv -= 45
					elif ((self.PXN + 1) in self.dun):
						dnumber = self.dun.index((self.PXN + 1))
						dname = self.dunN[dnumber]
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a dungeon. It looks like a " + dname + ".")
						self.output['text'] = stes
						self.twoyv -= 30
					else:
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "The only thing you see to the east is an endless evil fog.")
						self.output['text'] = stes
						self.twoyv -= 30
				#look west
				elif (a in self.westen):
					if ((self.PXN - 1) in self.wat):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see water.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((self.PXN - 1) in self.rou):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see rough.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((self.PXN - 1) in self.bun):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see bunker.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((self.PXN - 1) in self.fai):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see fairway.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((self.PXN - 1) in self.tow):
						tnumber = self.tow.index((self.PXN - 1))
						tname = self.towN[tnumber]
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a town, and can make out a distant sign. It reads: \n \" Welcome to " + tname + "\".")
						self.output['text'] = stes
						self.twoyv -= 45
					elif ((self.PXN - 1) in self.dun):
						dnumber = self.dun.index((self.PXN - 1))
						dname = self.dunN[dnumber]
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a dungeon. It looks like a " + dname + ".")
						self.twoyv -= 30
					else:
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "The only thing you see to the west is an endless evil fog.")
						self.output['text'] = stes
						self.twoyv -= 30
		#these are the cases where you look somewhere off the map
		def north():
			if((self.PXN - 9) < 1):
				stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "There is no land to the north. Only an endless evil fog.")
				self.output['text'] = stes
				self.twoyv -= 30
			else:
				self.PXN -= 9
				ee.look("here")
		def east():
			if((self.PXN + 1) > 81):
				stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "There is no land to the east. Only an endless evil fog.")
				self.output['text'] = stes
				self.twoyv -= 30
			else:
				self.PXN += 1
				ee.look("here")
		def south():
			if((self.PXN + 9) > 81):
				stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "There is no land to the south. Only an endless evil fog.")
				self.output['text'] = stes
				self.twoyv -= 30
			else:
				self.PXN += 9
				ee.look("here")
		def west():
			if((self.PXN - 1) < 1):
				stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "There is no land to the west. Only an endless evil fog.")
				self.output['text'] = stes
				self.twoyv -= 30
			else:
				self.PXN -= 1
				ee.look("here")
		#test function, tells you the number of the tile you are currently on
		def pxn():
			print(str(self.PXN))
		#describes items
		def desc(r):
			if (r == "a"):
				stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "this is the letter \'a\' from the latin alphabet.")
				self.output['text'] = stes
				self.twoyv -= 30
		#test function
		def AAAA():
			print("AAAA")		
		#print(self.output)
		entSp = ent.split(' ')	
		print(entSp)
		argd = {"test" : ee.printer, "look" : ee.look}
		argless = {"ha" : laugh, "North" : north, "north" : north, "N" : north, "n" : north, "S" : south, "s" : south, "south" : south, "South" : south, "e" : east, "E" : east, "east" : east, "East" : east, "w" : west, "W" : west, "west" : west, "West" : west, "index" : pxn, "exit": App.onClose}
		items = {"a", "here"}#<--- This is there so items/arguments in the game don't give an error when you put their names in a command
		for c in entSp:
			if c in argless:
				#command is issued, no further elaboration needed
				argless[c]()
				break
			elif c in argd:
				#command is issued using the word directly after the command as the argument
				argd[c](entSp[1])
				break
				
			elif c in items:
				#describe the item, or tells you it can't describe an argument.
				desc(entSp[0])
			else:
				entSpJ = " ".join(entSp)
				print(entSpJ)
				sterr = self.disp.set(self.disp.get() +"\n>" + entSpJ +"\n" + "I don't understand what you mean.")
				self.output['text'] = sterr
				print("42 >:(")
				print(c)
				x = len(entSp)
				self.twoyv -= (30)
				break
		self.output.place(y=self.twoyv)
		self.entry.delete(0,999)
	def onClose():
		root.destroy()
#these make the program go
app = App(root) 
root.protocol("WM_DELETE_WINDOW", App.onClose)
root.mainloop()
