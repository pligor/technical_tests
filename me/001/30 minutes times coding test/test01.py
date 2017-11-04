from __future__ import division
import re

#[for ii in ]
    #'[0-9]{2}:[0-9]{2}'

def solution(aa, bb):
    """https://codility.com/c/feedback/ZFFX7T-3HD"""
    # write your code in Python 2.7
    aa = str(aa)
    bb = str(bb)
    return str(bb).find(aa)


print solution(0, 2298)
print "test1 baby"