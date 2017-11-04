from __future__ import division

X = 1
Y = 10
D = 5


def solution(x, y, d):
    # write your code in Python 2.7

    myfloat = (y - x) / d
    myint = (y - x) // d

    if myfloat == myint: #exact division
        return myint
    else:
        return myint + 1


print solution(X, Y, D)
print "frog"
