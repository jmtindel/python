#!/usr/bin/python

import math
import os
import random
import re
import sys

def deal(n, counts=[0, 0]):
    for i in range(1, 11):
        if n+i > 21:    # bust
            counters[1] += 1
        elif n+i < 17:  # draw
            counts = deal(n+i, counts)
        else:           # stand
            counts[0] += 1
    return c

counts = deal(0)
print counts, sum(counts)
print float(c[1])/sum(c)
