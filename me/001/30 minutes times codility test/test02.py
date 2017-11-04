from __future__ import division
import numpy as np
A = [0] * 1
A[0] = 3

#integer M is the maximum value (not greated than M
#zero indexed array A

def solution(M, A):
    """https://codility.com/c/feedback/ZFFX7T-3HD"""
    N = len(A)
    count = [0] * (M + 1)

    maxOccurence = 1
    index = -1

    for i in xrange(N):
        if count[A[i]] > 0:
            count[A[i]] += 1; tmp = count[A[i]]
            if tmp > maxOccurence:
                maxOccurence = tmp
                index = i
        else:
            count[A[i]] = 1

    return A[index]

mm = 10000
#aa = [1,2,3,3,1,3,1]
aa = [4]
#aa = np.random.randint(1, mm, size=200000)
#print aa.shape
most_common_int = solution(mm, aa)
print most_common_int

aa = np.array(aa)
print len(aa[aa == most_common_int])

print "test 2 baby"