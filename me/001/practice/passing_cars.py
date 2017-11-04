from __future__ import division

A = [0] * 5

A[0] = 0
A[1] = 1
A[2] = 0
A[3] = 1
A[4] = 1


# 0 east
# 1 west

def solution(aa):
    # write your code in Python 2.7
    cur_mult = 0
    counter = 0
    start_elem = aa[0]
    elem = None
    left_overs = False
    init_left_overs = False
    for elem in aa:
        if counter > 1000000000:
            return -1

        if elem == start_elem:
            cur_mult += 1
            left_overs = True
        else:
            init_left_overs = True
            counter += cur_mult
            left_overs = False

    if left_overs and init_left_overs:
        counter += cur_mult
    return counter


A = [1, 0, 1, 0, 1, 1]
# 1 0
# 1 0

print solution(A)
print "passing cars baby!"
