from __future__ import division

A = [0] * 8
A[0] = 1
A[1] = 3
A[2] = 1
A[3] = 4
A[4] = 2
A[5] = 3
A[6] = 5
A[7] = 4


def solution(xx, aa):
    # write your code in Python 2.7
    positions = set(range(1, xx + 1))
    # print positions
    # print aa
    for ii, elem in enumerate(aa):
        try:
            positions.remove(elem)
        except:
            pass
        if len(positions) == 0:
            return ii

    return -1


# A=range(100000)
A = [5]
print solution(xx=5, aa=A)
print "DONE baby"
