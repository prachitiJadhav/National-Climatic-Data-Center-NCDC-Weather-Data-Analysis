#!/usr/bin/env python

import re
import sys

for line in sys.stdin:
  val = line.strip()
  (year, temp, q) = (val[4:10], val[78:84], val[84:85])
  if (temp != "999999" and re.match("[01459]", q)):
    print "%s\t%s" % (year, temp)
