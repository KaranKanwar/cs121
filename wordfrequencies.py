# Karan Kanwar - 68073357 - kkanwar
from collections import defaultdict
import sys
import re
import os

def printTokenCounts(fname):
	d = defaultdict(int)
	with open(fname, "r", encoding='utf-8') as ins:
		for line in ins:
		    for word in re.findall(r"[\w]+", line): # Regex matches every character class of A-z, 0-9 - will effectively split tokens which contain "-'!
	    		word = word.lower()
	    		d[word] += 1
	# Only sort dict once, nlogn complexity
	sortedDict = sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))
	# n complexity
	unicodeError = 0
	for k, v in sortedDict:
		try:
			print(k, "-", v)
		except UnicodeEncodeError:
			unicodeError = 1
			pass
	if(unicodeError == 1):
		print("Warning: Unsupported unicode characters were found")
	# Empirical time testing suggests will be able to handle larger file

if __name__ == "__main__":
	fname = ""
	try:
		fname = sys.argv[1]
	except IndexError:
		pass
	if(fname == ""):
		raise Exception("A file must be provided, e.g. wordfrequencies.py file.txt")
	if os.path.exists(fname) and os.path.getsize(fname) > 0:
		printTokenCounts(fname)
	else:
		raise Exception("The provided file is either empty or does not exist")
