from nltk.corpus import wordnet as wn


def findPos():
	print (wn.synsets('hello'))
	syns = wn.synsets('sarcasm')
	print "synsets:", syns
	for s in syns:
		for l in s.lemmas:
			print l.name
    	print s.definition
    	print s.examples















if __name__ == "__main__":
    findPos()