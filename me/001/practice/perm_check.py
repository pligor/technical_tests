from __future__ import division

A = [0] * 3
A[0] = 4
A[1] = 1
A[2] = 3
#A[3] = 2

def solution(aa):
    # write your code in Python 2.7
    return 0 if len(set(range(1, len(aa) + 1)).difference(aa)) > 0 else 1


A=range(1, 10)
print solution(A)
print "perm check baby"