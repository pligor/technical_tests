from __future__ import division

A = [0] * 7
A[0] = 3
A[1] = 4
A[2] = 4
A[3] = 6
A[4] = 1
A[5] = 4
A[6] = 4

#N counters
#set to zero
#increase counter 3
#increase counter 4

#set to maximum value

def solution(nn, aa):
    # write your code in Python 2.7
    cc = [0] * nn

    max_elem = float('-inf')
    for elem in aa:
        if elem <= nn:
            ind = elem - 1
            cc[ind] += 1
            max_elem = max(cc[ind], max_elem)
        else:
            if max_elem != float('-inf'):
                cc = [max_elem] * nn #reset with maximum element

    return cc


A = [3,6]
print solution(nn=5, aa=A)
print "max counters baby"