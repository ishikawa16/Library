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


def update(k, x):
    '''
    a[k]の値をxに更新
    O(logN)
    '''
    k += num - 1
    seg[k] = x
    while k:
        k = (k - 1) // 2
        seg[k] = segfunc(seg[k*2+1], seg[k*2+2])


def query(p, q):
    '''
    [p, q)についてsegfuncを適用したものを返す
    O(logN)
    '''
    if q <= p:
        return ide_ele
    
    p += num - 1
    q += num - 2
    res = ide_ele

    while q - p > 1:
        if p & 1 == 0:
            res = segfunc(res, seg[p])
        if q & 1 == 1:
            res = segfunc(res, seg[q])
            q -= 1
        p = p // 2
        q = (q - 1) // 2
    
    if p == q:
        res = segfunc(res, seg[p])
    else:
        res = segfunc(res, segfunc(seg[p], seg[q]))
    
    return res


################################
n = 8                             # 要素数
num = (2 ** len(bin(n - 1)) - 2)  # n以上の最小の2のべき乗
ide_ele = float('inf')            # 単位元(最小値のセグ木:inf, 最大値のセグ木:-1, 和のセグ木:0, 積のセグ木:1, gcdのセグ木:0)
seg = [ide_ele] * 2 * num