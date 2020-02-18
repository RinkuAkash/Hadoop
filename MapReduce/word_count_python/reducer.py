#!/usr/bin/env python3

from operator import itemgetter
import sys

# Word count python reducer code

word2count = {}

for line in sys.stdin:
    line = line.strip()
    word, count = line.split(',')
    count = int(count)
    try:
        word2count[word] = word2count[word]+count
    except:
        word2count[word] = count
for word in word2count.keys():
    print("%s\t%s"%(word, word2count[word]))

