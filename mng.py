#!usr/bin/python
from random import *
import linecache
import math

def generator():
	initF = uniform(0,58110)
	numF = round(initF,0)
	realF = math.floor(numF)
	print(numF)
	initL = uniform(1,16)
	numL = round(initL,0)
	realL = math.floor(numL)
	print(numL)
	first = linecache.getline("./NameTable/Name1",realF)
	print(first)
	first = first[:-1]
	last = linecache.getline("./NameTable/monsterName",realL)
	print(last)
	last = last[:-1]
	monsname = (first + " " + last)
	return monsname
