#!/usr/bin/env python3

import sys
import re

# Word count python mapper code

for line in sys.stdin:
    line = line.strip()
    words = re.findall("[\w']+", line)
    for word in words:
        print('%s,%s' % (word, 1))
