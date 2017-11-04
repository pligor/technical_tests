from __future__ import division

ss = 'CAGCCTA'
pp = [2, 5, 0]
qq = [4, 5, 6]


def slow_solution(ss, pp, qq):
    # write your code in Python 2.7
    ss = ss.replace('A', '1')
    ss = ss.replace('C', '2')
    ss = ss.replace('G', '3')
    ss = ss.replace('T', '4')
    ints = map(lambda xx: int(xx), list(ss))
    # print ints

    answer = []
    for start, stop in zip(pp, qq):
        answer.append(
            min(ints[start: stop + 1])
        )

    return answer


def solution(ss, pp, qq):
    # write your code in Python 2.7

    lex = {
        'A': 1,
        'C': 2,
        'G': 3,
        'T': 4
    }

    answer = [float('inf')] * len(pp)

    mapper = lambda xx: lex[xx]

    for jj, elem in enumerate(ss):
        for ii, (start, stop) in enumerate(zip(pp, qq)):
            if start <= jj <= stop:
                answer[ii] = min(answer[ii], mapper(elem))

    return answer

print slow_solution(ss, pp, qq)
print solution(ss, pp, qq)

print "DONE baby"
