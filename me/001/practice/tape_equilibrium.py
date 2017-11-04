from __future__ import division

A = [0] * 5
A[0] = 3
A[1] = 1
A[2] = 2
A[3] = 4
A[4] = 3

def dummy_solution(a):
    # write your code in Python 2.7
    # 24810
    return min([abs(sum(a[:pp]) - sum(a[pp:])) for pp in range(1, len(a)-1)])


def solution(aa):
    # write your code in Python 2.7

    left_sum = 0
    right_sum = sum(aa)
    min_diff = float('inf')

    for elem in aa:
        left_sum += elem
        right_sum -= elem
        min_diff = min(abs(left_sum - right_sum), min_diff)

    return min_diff


A=range(100000)
print solution(A)
print "tape equilibrium"