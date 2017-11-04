from __future__ import division


def solution(aa):
    # write your code in Python 2.7

    aa = filter(lambda xx: xx > 0, aa)  # remove negatives
    if len(aa) == 0:
        return 1

    maximum = max(aa) + 1
    maximum = max(maximum, 1)  # for the extreme case where all are negatives

    not_in_aa = set(range(1, maximum + 1)).difference(aa)

    return min(not_in_aa)

#A = [1, 3, 6, 4, 1, 2]
#A = [1, 2, 3]
#A = [-1, -2, -3]
A = [0, 0]
print solution(A)
print "missing int baby"
