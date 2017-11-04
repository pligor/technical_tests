from __future__ import division

A = [0] * 5
B = [0] * 5
A[0] = 4;    B[0] = 0
A[1] = 3;    B[1] = 1
A[2] = 2;    B[2] = 0
A[3] = 1;    B[3] = 0
A[4] = 5;    B[4] = 0

#P and Q are two
#P < Q P upstream of fish Q
#0 represents fish upstreaam
#1 downstream

def solution(aa, bb):
    # write your code in Python 2.7

    while len(bb) > 0:
        try:
            one_ind = next(ii for ii in xrange(len(bb)) if bb[ii] == 1)
            #print one_ind
            zero_ind = next(jj for jj in xrange(one_ind+1, len(bb)) if bb[jj] == 0) + one_ind - 1
            #print zero_ind
            small_fish = one_ind if aa[one_ind] < aa[zero_ind] else zero_ind
            del aa[small_fish]
            del bb[small_fish]
        except StopIteration:
            print "stop"
            break

    return len(bb)


print solution(A, B)
print "fish baby"