#!/usr/bin/python

import os
import struct
import argparse
import random
import math
import sys

parser=argparse.ArgumentParser(description="Create random password from dictionary (a la 'correct horse battery staple')", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--count", "-c", type=int, default=4, help="Number of words")
parser.add_argument("--maxlen", "-m", type=int, help="Restrict dictionary to words with up to maxlen letters")
parser.add_argument("--dictionary", "-d", choices=["german", "british", "american"], default="german", help="Which dictionary to use")
args = parser.parse_args()

dict_path = "/usr/share/dict"

rand_gen = random.SystemRandom()

if args.dictionary == "german":
	fname = "ngerman"
elif args.dictionary == "british":
	fname = "british-english"
else:
	fname = "american-english"

try:
	with open(os.path.join(dict_path, fname)) as f:
		dictionary = list(f)
except IOError:
	print >> sys.stderr, "Dictionary {} not found in /usr/share/dict".format(fname)
	sys.exit(1)
	
if args.maxlen != None:
	dictionary = [word for word in dictionary if len(word) <= args.maxlen]
dictionary_length = len(dictionary)

print "dictionary length:", dictionary_length
print "Entropy:", math.log(dictionary_length**args.count, 2), "bits"
for i in xrange(args.count):
	print dictionary[rand_gen.randint(0, dictionary_length-1)][:-1],
print ""
