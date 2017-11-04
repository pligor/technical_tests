# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N):
    # write your code in Python 2.7
    bstr = format(N, 'b')

    #count = 0
    splits = bstr.split('1')
    #print splits

    # if bstr[0] == '1' and bstr[-1] == '1':
    lens = [(len(cur), ii) for ii, cur in enumerate( splits )]
    #return lens
    #print lens

    def keyf(xx, yy):
        #print elem
        return xx[0] - yy[0]

    #sorted_lens = sorted(lens, lambda xx, yy : xx)
    sorted_lens = sorted(lens, keyf, reverse=True)

    #return sorted_lens
    #print sorted_lens

    final_len = 0
    for cur_len, cur_ind in sorted_lens:
        if 0 < cur_ind < len(sorted_lens) - 1:
            return cur_len

    return final_len
    # else:
    #     return 0


assert solution(9) == 2
assert solution(529) == 4
assert solution(20) == 1
assert solution(15) == 0
print "OK"
