#!usr/bin/python
from random import *
import linecache
import math

def generator():
	initF = uniform(1,2000)
	numF = round(initF,0)
	realF = math.floor(numF)
	print(numF)
	initL = uniform(1,88305)
	numL = round(initL,0)
	realL = math.floor(numL)
	print(numL)
	first = linecache.getline("./NameTable/firstname",realF)
	print(first)
	first = first[:-1]
	last = linecache.getline("./NameTable/surname",realL)
	print(last)
	last = last[:-1]
	persname = (first + " " + last)
	return persname
