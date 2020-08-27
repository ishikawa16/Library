# Segment Tree

def segfunc(x, y):
    '''
    問題に応じて返り値を設定
    '''
    return min(x, y)


def init(a):
    '''
    配列aで初期化
    '''
    for i in range(n):
        seg[i+num-1] = a[i]    
    for i in range(num-2, -1, -1) :
        seg[i] = segfunc(seg[2*i+1], seg[2*i+2])


def query(l, r):
    '''
    [l, r)についてsegfuncを適用したものを求める
    O(logN)
    '''
    if r <= l:
        return ide_ele
    
    l += num - 1
    r += num - 2
    res = ide_ele

    while r - l > 1:
        if l & 1 == 0:
            res = segfunc(res, seg[l])
        if r & 1 == 1:
            res = segfunc(res, seg[r])
            r -= 1
        l = l // 2
        r = (r - 1) // 2
    
    if l == r:
        res = segfunc(res, seg[l])
    else:
        res = segfunc(res, segfunc(seg[l], seg[r]))
    
    return res


def update(i, x):
    '''
    a[i]の値をxに更新
    O(logN)
    '''
    i += num - 1
    seg[i] = x
    while i:
        i = (i - 1) // 2
        seg[i] = segfunc(seg[i*2+1], seg[i*2+2])



n = 6                             # 要素数
num = (2 ** len(bin(n - 1)) - 2)  # n以上の最小の2の累乗
ide_ele = float('inf')            # 単位元(最小値のセグ木:inf, 最大値のセグ木:-1, 和のセグ木:0, 積のセグ木:1, gcdのセグ木:0)
seg = [ide_ele] * 2 * num

'''
a = [3, 1, 7, 4, 9, 2]
init(a)

query(1, 4)
> 1

update(1, 6)

query(1, 4)
> 4
'''