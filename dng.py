#!usr/bin/python
from random import *
import linecache
import math

def generator():
	initF = uniform(0,58110)
	numF = round(initF,0)
	realF = math.floor(numF)
	print(numF)
	initL = uniform(1,50)
	numL = round(initL,0)
	realL = math.floor(numL)
	print(numL)
	first = linecache.getline("./NameTable/Name1",realF)
	print(first)
	first = first[:-1]
	last = linecache.getline("./NameTable/dungeonName",realL)
	print(last)
	last = last[:-1]
	dungname = (first + last)
	return dungname
