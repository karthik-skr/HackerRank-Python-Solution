def formingMagicSquare(s):
	square = []
	for i in s:
		square += i
	print(square)
	totalSum = sum([i for i in range(1,10)])
	rowSum = totalSum//3
	print(rowSum)
	grps = getMagicGroups(rowSum)
	counts = {}
	for g in grps:
		for n in g:
			counts[n] = counts.get(n,0)+1
	countSizes = {}
	for c in counts.items():
		if c[1] not in countSizes:
			countSizes[c[1]] = []
		countSizes[c[1]].append(c[0])

	print(countSizes)
	valid1 = []
	valid2 = []
	for i,v1 in enumerate(countSizes[3]):
		for v2 in countSizes[3][i+1:]:
			for v3 in countSizes[2]:
				if sum([v1,v3,v2]) == rowSum:
					valid1.append([v1,v3,v2])
					valid1.append([v2,v3,v1])
	
	for j,v5 in enumerate(countSizes[2]):
		for v6 in countSizes[2][j+1:]:
			for v4 in countSizes[4]:
				if sum([v5,v4,v6]) == rowSum:
					valid2.append([v5,v4,v6])
					valid2.append([v6,v4,v5])

	print(valid1,"\n",valid2,"\n")
	magicSquares = []
	for i1,v1 in enumerate(valid1):
		for v12 in valid1[i1+1:]:
			if len(set(v1)-set(v12)) == 3:
				# print(v1,v12)
				for v3 in valid2:
					if(len(set(v3)-set(v1+v12)) == 3):
						if(v1[0]+v3[0]+v12[0] == rowSum):
							magicSquares.append(v1+v3+v12)
							magicSquares.append(list(reversed(v1+v3+v12)))

	print(magicSquares,square)
	minDiff = 99
	for magicSquare in magicSquares:
		diff = 0
		for i in range(9):
			diff += abs(magicSquare[i] - square[i])
		minDiff = diff if diff < minDiff else minDiff
		print(diff)
	return (minDiff)

def getMagicGroups(rowSum):
	grps = []
	for i in range(1,10):
		for j in range(i+1,10):
			for k in range(j+1,10):
				if(sum([i,j,k]) == rowSum):
					grps.append([i,j,k])
	return grps
if __name__ == '__main__':
	print(formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]]))