#!/bin/python3


def nonDivisibleSubset(k, S):
	L = [0]*k
	for x in S: 
		L[x % k] += 1
	res = 0
	print(L)
	for i in range(k//2+1):
		# print(i,"i")
		if i == 0 or k == i*2:
			res += bool(L[i])
		else:
			res += max(L[i], L[k-i])
	return res

if __name__ == '__main__':
	print(nonDivisibleSubset(3,[1,7,2,4]))
