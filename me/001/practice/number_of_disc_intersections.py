from __future__ import division

A = [0] * 6
A[0] = 1
A[1] = 5
A[2] = 2
A[3] = 1
A[4] = 4
A[5] = 0


def do_intersect(disc1, disc2):
    disc1_is_left_to_disc2 = disc1[1] < disc2[0]
    disc1_is_right_to_disc2 = disc2[1] < disc1[0]
    return not (disc1_is_left_to_disc2 or disc1_is_right_to_disc2)


def slow_solution(aa):
    # write your code in Python 2.7

    # for two discs to intersect they need to have their radius overlapping or just overlapping
    # 1-5, 1+5 is a region you could find other values
    # convert all into regions
    regions = [(ii - elem, ii + elem) for ii, elem in enumerate(aa)]
    counter = 0
    for ii, region_a in enumerate(regions):
        for region_b in regions[ii + 1:]:
            counter += do_intersect(region_a, region_b)

    return counter

def solution(aa):
    # write your code in Python 2.7

    # for two discs to intersect they need to have their radius overlapping or just overlapping
    # 1-5, 1+5 is a region you could find other values
    # convert all into regions
    regions = [(ii - elem, ii + elem) for ii, elem in enumerate(aa)]
    counter = 0
    for ii, region_a in enumerate(regions):
        for region_b in regions[ii + 1:]:
            counter += do_intersect(region_a, region_b)

    return counter

print slow_solution(A)
print solution(A)
print "num disc intersect baby"
