A = [0] * 7
A[0] = 9
A[1] = 3
A[2] = 9
A[3] = 3
A[4] = 9
A[5] = 7
A[6] = 9


# def solution(A):
#     # write your code in Python 2.7
#     nopair = None
#     for ii in A[:-1]:
#         nopair = ii
#         for jj in A[ii+1:]:
#             if nopair == jj:
#                 nopair = None
#
#     return nopair

def solution(A):
    # write your code in Python 2.7
    # nopair = None

    dd = set()

    # for each element check to see if there is the same match, somewhere
    # if there is then
    # start using a dictionary to save element positions
    # so 9 is at position 0 etc.
    # then try to delete. if failing to delete then add this to the map

    # print dd[9]

    for num in A:
        try:
            dd.remove(num)
        except:
            dd.add(num)

        #print dd

    return list(dd)[0]


# N integers
# odd number of elements

print A
print solution(A)
# assert hello() == 0
# print "OK"
