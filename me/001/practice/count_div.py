from __future__ import division
import math
A = [0] * 1
A[0] = 3

def dummy_solution(aa, bb, kk):
    # write your code in Python 2.7
    return sum([1 for elem in range(aa, bb+1) if elem % kk == 0])

def solution(aa, bb, kk):
    # write your code in Python 2.7
    diff = bb - aa
    if diff < kk:
        return 1

    res = (bb - aa + 1) / kk
    print res
    #return int(round(res))
    integer = int(round(res))
    return integer + 1 if aa == 0 else integer

# print dummy_solution(6, 11, 2)
# print solution(6, 11, 2)
import sys
aa = 100
bb = 123000000
kk = 10000
print dummy_solution(aa, bb, kk)
print solution(aa, bb, kk)
print "count div baby"
