import string

def biggerIsGreater(w):
    letterMap = {}
    idList = []
    for i in list(w):
        ind = string.ascii_lowercase.index(i)
        letterMap[ind] = i
        idList.append(ind)

    i = len(idList) - 1
    while i > 0 and idList[i - 1] >= idList[i]:
        i -= 1
    if i <= 0:
        return "no answer"
    
    print(idList)
    j = len(idList) - 1
    while idList[j] <= idList[i - 1]:
        j -= 1
    idList[i - 1], idList[j] = idList[j], idList[i - 1]
    
    # Reverse suffix
    print(idList,idList[i:],len(idList)-1,i-1)
    idList[i : ] = idList[len(idList) - 1 : i - 1 : -1]
    print(idList)
    letterList = [letterMap[v] for v in idList]


    return ''.join(letterList)

if __name__ == '__main__':
   
	result = biggerIsGreater("dkhc")

	print(result)