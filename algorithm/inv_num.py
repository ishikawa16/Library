# Inversion Number

from bisect import bisect_left


def inv_num(a):
    '''
    配列の転倒数を求める
    O(NlogN)
    '''
    a = compress(a)

    res = 0
    for i, v in enumerate(a):
        res += i - query(v+1)
        update(v+1, 1)
    
    return res


def query(i):
    '''
    a[0] + a[1] + … + a[i-1] を求める
    O(logN)
    '''
    res = 0
    while i > 0:
        res += BIT[i]
        i -= i & -i
    
    return res


def update(i, x):
    '''
    a[i-1]にxを加算
    O(logN)
    '''
    while i <= n:
        BIT[i] += x
        i += i & -i


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



n = 5  # 要素数
a = [3, 1, 5, 4, 2]
BIT = [0] * (n+1)

'''
inv_num(a)
> 5
'''