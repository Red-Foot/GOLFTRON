#!usr/bin/python
#haha yes
import tkinter as tk
from tkinter import Frame
import linecache as lc

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
		#initializes which tiles are which kind
		with open("worldtypes") as worldmap:
			self.wat = str(lc.getline('worldtypes', 3))
			self.rou = str(lc.getline('worldtypes', 5))
			self.bun = str(lc.getline('worldtypes', 7))
			self.fai = str(lc.getline('worldtypes', 9))
			self.tow = str(lc.getline('worldtypes', 11))
			self.dun = str(lc.getline('worldtypes', 13))
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
		self.wat
		self.rou
		self.bun
		self.fai
		self.tow
		self.dun
		self.nord
		self.sud
		self.ost
		self.westen
		def laugh():
			sha = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "ha")
			self.output['text'] = sha
			self.twoyv -= 30
		class ee:
			def printer(a):
				stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + a)
				self.output['text'] = stes
				self.twoyv -= 30
			def look(a):
				if (a == "here"):
					if ((" " + str(self.PXN)+ ",") in self.wat):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You're in water.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str(self.PXN)+ ",") in self.rou):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You're in rough.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str(self.PXN)+ ",") in self.bun):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You're in bunker.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str(self.PXN)+ ",") in self.fai):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You're in fairway.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN - 9))+ ",") in self.tow):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You're in town.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str(self.PXN)+ ",") in self.dun):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You're in dungeon.")
						self.output['text'] = stes
						self.twoyv -= 30
				elif (a in self.nord):
					if ((" " + str((self.PXN - 9))+ ",") in self.wat):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see some water.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN - 9))+ ",") in self.rou):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a rough.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN - 9))+ ",") in self.bun):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a bunker.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN - 9))+ ",") in self.fai):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a fairway.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN - 9))+ ",") in self.tow):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a town.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN - 9))+ ",") in self.dun):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a dungeon.")
						self.output['text'] = stes
						self.twoyv -= 30
					else:
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "The only thing you see to the north is an endless evil fog.")
						self.output['text'] = stes
						self.twoyv -= 30
				elif (a in self.sud):
					if ((" " + str((self.PXN + 9))+ ",") in self.wat):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see some water.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN + 9))+ ",") in self.rou):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a rough.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN + 9))+ ",") in self.bun):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a bunker.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN + 9))+ ",") in self.fai):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a fairway.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN + 9))+ ",") in self.tow):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a town.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN + 9))+ ",") in self.dun):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a dungeon.")
						self.output['text'] = stes
						self.twoyv -= 30
					else:
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "The only thing you see to the south is an endless evil fog.")
						self.output['text'] = stes
						self.twoyv -= 30
				elif (a in self.ost):
					if ((" " + str((self.PXN + 1))+ ",") in self.wat):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see some water.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN + 1))+ ",") in self.rou):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a rough.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN + 1))+ ",") in self.bun):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a bunker.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN + 1))+ ",") in self.fai):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a fairway.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN + 1))+ ",") in self.tow):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a town.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN + 1))+ ",") in self.dun):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a dungeon.")
						self.output['text'] = stes
						self.twoyv -= 30
					else:
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "The only thing you see to the east is an endless evil fog.")
						self.output['text'] = stes
						self.twoyv -= 30
				elif (a in self.westen):
					if ((" " + str((self.PXN - 1))+ ",") in self.wat):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see some water.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN - 1))+ ",") in self.rou):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a rough.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN - 1))+ ",") in self.bun):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a bunker.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN - 1))+ ",") in self.fai):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a fairway.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN - 1))+ ",") in self.tow):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a town.")
						self.output['text'] = stes
						self.twoyv -= 30
					elif ((" " + str((self.PXN - 1))+ ",") in self.dun):
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "You see a dungeon.")
						self.output['text'] = stes
						self.twoyv -= 30
					else:
						stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "The only thing you see to the west is an endless evil fog.")
						self.output['text'] = stes
						self.twoyv -= 30
		def north():
			if((self.PXN - 9) < 1):
				stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "There is no land to the north. Only an endless evil fog.")
				self.output['text'] = stes
				self.twoyv -= 30
			else:
				self.PXN -= 9
				stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "you went north")
				self.output['text'] = stes
				self.twoyv -= 30
		def east():
			if((self.PXN + 1) > 81):
				stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "There is no land to the east. Only an endless evil fog.")
				self.output['text'] = stes
				self.twoyv -= 30
			else:
				self.PXN += 1
				stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "you went east")
				self.output['text'] = stes
				self.twoyv -= 30
		def south():
			if((self.PXN + 9) > 81):
				stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "There is no land to the south. Only an endless evil fog.")
				self.output['text'] = stes
				self.twoyv -= 30
			else:
				self.PXN += 9
				stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "you went south")
				self.output['text'] = stes
				self.twoyv -= 30
		def west():
			if((self.PXN - 1) < 1):
				stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "There is no land to the west. Only an endless evil fog.")
				self.output['text'] = stes
				self.twoyv -= 30
			else:
				self.PXN -= 1
				stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "you went west")
				self.output['text'] = stes
				self.twoyv -= 30
		def pxn():
			print(str(self.PXN))
		def desc(r):
			if (r == "a"):
				stes = self.disp.set(self.disp.get() + "\n>" + ent + "\n" + "this is the letter \'a\' from the latin alphabet.")
				self.output['text'] = stes
				self.twoyv -= 30
		#print(self.output)
		entSp = ent.split(' ')	
		print(entSp)
		argd = {"test" : ee.printer, "look" : ee.look}
		argless = {"ha" : laugh, "North" : north, "north" : north, "N" : north, "n" : north, "S" : south, "s" : south, "south" : south, "South" : south, "e" : east, "E" : east, "east" : east, "East" : east, "w" : west, "W" : west, "west" : west, "West" : west, "index" : pxn}
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
				print("42")
				print(c)
				x = len(entSp)
				self.twoyv -= (30)
				break
		self.output.place(y=self.twoyv)
		self.entry.delete(0,999)
#these make the program go
app = App(root) 
root.mainloop()