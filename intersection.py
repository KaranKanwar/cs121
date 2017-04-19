# Karan Kanwar - 68073357 - kkanwar
import sys
import re
import os

def getTokens(fname):
	d = set()
	with open(fname, "r") as ins:
		for line in ins:
		    for word in re.findall(r"[\w]+", line): # Regex matches every character class of A-z, 0-9 - will effectively split tokens which contain "-'!
	    		d.add(word.lower())
	return d

if __name__ == "__main__":
	fname1 = ""
	fname2 = ""
	try:
		fname1 = sys.argv[1]
		fname2 = sys.argv[2]
	except IndexError:
		pass
	if(fname1 == "" or fname2 == ""):
		raise Exception("Two files must be provided, e.g. intersection.py file1.txt file2.txt, please fix this and try again")
	if os.path.exists(fname1) and os.path.getsize(fname1) and os.path.exists(fname2) and os.path.getsize(fname2) > 0:
		print(len(getTokens(fname1).intersection(getTokens(fname2))))
	else:
		raise Exception("One or more of the provided files is either empty or does not exist, please fix this and try again")