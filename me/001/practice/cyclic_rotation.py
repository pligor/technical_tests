A = [3, 8, 9, 7, 6]
#A = []

def solution(A, K):
    # write your code in Python 2.7
    a = A

    if len(a) == 0:
        return a

    k = K%len(a)

    #print list(reversed(a[-k:])) + a[:-k]
    return a[-k:] + a[:-k]


print solution(A, K=6)