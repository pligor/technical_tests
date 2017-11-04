from __future__ import division

A = [0] * 1
A[0] = 3


# decimal zip

def solution(aa, bb):
    """https://codility.com/c/feedback/ZFFX7T-3HD"""
    # write your code in Python 2.7
    aa = str(aa)
    bb = str(bb)

    common_len = min(len(aa), len(bb))

    prefix_aa = aa[:common_len]
    prefix_bb = bb[:common_len]
    postfix_aa = aa[common_len:]
    postfix_bb = bb[common_len:]

    print postfix_aa
    print postfix_bb

    print prefix_aa
    print prefix_bb
    res = "".join(["".join(tpl) for tpl in zip(aa, bb)]) + postfix_aa + postfix_bb

    print res

    res = int(res)

    if res > int(1e8):
        return -1

    return res


A = int(1e2)
B = int(1e4)
print solution(A, B)
print "test 3 baby"
