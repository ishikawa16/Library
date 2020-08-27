# Weighted Union-Find Tree

def find(x):
    '''
    xの根を求める
    O(α(N))
    '''
    if par[x] < 0:
        return x
    else:
        p = find(par[x])
        diff_w[x] += diff_w[par[x]]
        par[x] = p
        return p


def weight(x):
    '''
    xの根からの距離を求める
    '''
    find(x)
    return diff_w[x]


def union(x, y, w):
    '''
    weight(y) - weight(x) = w となるようにxとyの属する集合を併合する
    '''
    w += weight(x) - weight(y)
    x = find(x)
    y = find(y)
    
    if x == y:
        return False

    if par[x] > par[y]:
        x, y = y, x
        w = -w
    par[x] += par[y]
    par[y] = x
    diff_w[y] = w
    return True


def same(x, y):
    '''
    xとyが同じ集合に属するかを判定する
    '''
    return find(x) == find(y)


def size(x):
    '''
    xが属する集合の個数を求める
    '''
    return -par[find(x)]


def diff(x, y):
    '''
    xとyが同じ集合に属するときの w[y] - w[x] を求める
    '''
    return weight(y) - weight(x)



v = 6             # 頂点数
par = [-1] * v    # 根:-size, 葉:親の頂点
diff_w = [0] * v  # 根:0, 葉:親からの距離

'''
union(0, 1, 4)
union(0, 3, 6)
union(1, 4, 8)

weight(4)
> 12

diff(1, 3)
> 2
'''