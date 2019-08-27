#!usr/bin/python
from random import *
import linecache
import math

def generator():
	initF = uniform(1,58110)
	numF = round(initF,0)
	realF = math.floor(numF)
	print(numF)
	initL = uniform(1,58110)
	numL = round(initL,0)
	realL = math.floor(numL)
	print(numL)
	adj = linecache.getline("./NameTable/Name1",realF)
	print(adj)
	adj = adj[:-1]
	nou = linecache.getline("./NameTable/Name1",realL)
	print(nou)
	nou = nou[:-1]
	storename = ("the " + adj + " " + nou)
	return storename
