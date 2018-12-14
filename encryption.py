import math
def encryption(s):
	s = ''.join(s.split(" "))
	l = len(s)
	rows = math.floor(l**(1/2))
	cols = math.ceil(l**(1/2))
	arr1 = []
	end = 0
	while  end <= l:
		arr1.append(s[end:end+cols])
		end = end+cols
	resObj = {}
	for v1 in arr1:
		for i,v2 in enumerate(v1):
			print(i,v2)
			resObj[i] = resObj.get(i,'')+v2
	return " ".join(resObj.values())
if __name__ == '__main__':
    result = encryption("feedthedog")
    print(result,"result")