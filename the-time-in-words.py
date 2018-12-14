
def timeInWords(h, m):
	words = {1: "one", 2: "two",   3: "three", 4: "four",  5: "five",
		 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
		 11: "eleven",   12: "twelve",  13: "thirteen",   14: "fourteen",
		 15: "fifteen",  16: "sixteen", 17: "seventeen",  18: "eighteen",
		 19: "nineteen", 20: "twenty",  21: "twenty one", 22: "twenty two",
		 23: "twenty three", 24: "twenty four",  25: "twenty five",
		 26: "twenty six",   27: "twenty seven", 28: "twenty eight",
		 29: "twenty nine"}
	if m == 0:
		return words[h] + " o' clock"
		sys.exit()
	elif m == 30:
		return "half past "+words[h]
	if m < 30:
		if m == 1:
			return "one minute past "+ words[h]
		elif m == 15:
			return "quarter past "+ words[h]
		else:
			return words[m]+" minutes past "+ words[h]
	else:
		m = 60 - m
		h += 1
		if m == 1:
			return "one minute to "+ words[h]
		elif m == 15:
			return "quarter to "+words[h]
		else:
			return words[m] +" minutes to "+ words[h]

if __name__ == '__main__':
	
	result = timeInWords(5, 45)

	print(result)

