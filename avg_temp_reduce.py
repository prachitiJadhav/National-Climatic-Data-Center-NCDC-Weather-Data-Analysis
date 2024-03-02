#!/usr/bin/env python

import sys

(last_key, max_val,c) = (None, 0, 0)
for line in sys.stdin:
  (key, val) = line.strip().split("\t")
  if last_key and last_key != key:
    print "%s\t%s" % (last_key, max_val/c)
    (last_key, max_val,c) = (key, int(val),1)
  else:
    (last_key, max_val,c) = (key, int(max_val)+int(val),c+1)

if last_key:
  print "%s\t%s" % (last_key, max_val/c)