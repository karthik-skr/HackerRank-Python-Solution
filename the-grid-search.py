#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):
	G_r = len(G)
	G_c = len(G[0])
	P_r = len(P)
	P_c = len(P[0])
	for r in range(0,G_r - P_r +1):
		rows = G[r:r+P_r]
		resRow = []
		for c in range(0,G_c-P_c+1):
			pattern = []
			isNot = False
			for i,r in enumerate(rows):
				rowSlc = r[c:c+P_c]
				if(P[i] != rowSlc):
					isNot = True
					break
			if(isNot == False):
				return "YES"

	return "NO"

if __name__ == '__main__':
	result = gridSearch(['7283455864', '6731158619', '8988242643', '3830589324', '2229505813', '5633845374', '6473530293', '7053106601', '0834282956', '4607924137'], ['9505', '3845', '3530'])
	print("result",result)