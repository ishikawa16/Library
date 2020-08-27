# LIS: Longest Increasing Subsequence

from bisect import bisect_left


def LIS(seq):
    '''
    最長増加部分列の長さを求める
    O(NlogN)
    '''
    l = [seq[0]]
    for v in seq:
        if l[-1] < v:
            l.append(v)
        else:
            l[bisect_left(l, v)] = v

    return len(l)



'''
a = [1, 5, 3, 6, 2, 4, 8, 7]
LIS(a)
> 4
'''