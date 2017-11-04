A = [0] * 4
A[0] = 2
A[1] = 3
A[2] = 1
A[3] = 5

A = [1,2]

def solution(A):
    # write your code in Python 2.7
    if len(A) == 0:
        return 0
    elif len(A) == 1:
        return 1

    thelist = list(set(range(1, len(A)+1+1)).difference(A))
    if len(thelist) == 0:
        return 0
    else:
        return thelist[0]

print solution(A)