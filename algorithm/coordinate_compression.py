# Coordinate Compression

from bisect import bisect_left


def compress(a):
    '''
    配列の大小関係を抽出する(1次元圧縮)
    O(NlogN)
    '''
    tmp = sorted(list(set(a)))
    res = []
    for v in a:
        res.append(bisect_left(tmp, v))
    
    return res



'''
a = [1, 4, 3, 4, 8, 6]
compress(a)
> [0, 2, 1, 2, 4, 3]
'''