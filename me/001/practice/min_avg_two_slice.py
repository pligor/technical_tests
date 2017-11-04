from __future__ import division
import numpy as np


def slow_solution(aa):
    tpls = [(sum(aa[slice(ii, jj + 1)]) / (jj - ii), ii) for ii in range(len(aa)) for jj in range(len(aa)) if ii < jj]
    # print tpls[:10]
    sort_tpls = sorted(tpls, key=lambda xx: xx[0])

    return sort_tpls[0][1]


def solution(aa):
    # write your code in Python 2.7

    min_start = 0

    minimals = [float('inf')] * len(aa)
    minimals[0] = sum(aa[:2])
    for ii, elem in enumerate(aa[2:]):
        # add to current sum
        # if new sum is smaller then save this as current sum and go to next
        # if new sum is larger then this means we should move the min_start to the next element
        # we also need to save new sum as current sum but subtract the element that was at min_start
        # we also need to save for the min_start in minimals

        cur_sum = minimals[min_start]
        new_sum = minimals[min_start] + elem
        cur_len = ii - min_start + 1

        if (new_sum / cur_len) < (cur_sum / cur_len):
            for ind in range(min_start, ii):
                if minimals[ind] == float('inf'): #enable cell
                    minimals[ind] = 0

                minimals[ind] += elem
        else:
            minimals[min_start] = cur_sum / cur_len
            cur_sum = new_sum - aa[min_start]
            min_start += 1

    return sorted(minimals.iteritems(), key=lambda xx: xx[1])[0][0]


# A = list(np.random.randint(-10000, 10000, 100000))
A = [4, 2, 2, 5, 1, 5, 8]
# print slow_solution(A)
print solution(A)
print "min avg baby"
