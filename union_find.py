# Union-Find Tree

def find(x):
    '''
    xの根を求める
    O(α(N))
    '''
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def union(x, y):
    '''
    xとyの属する集合を併合する
    '''
    x = find(x)
    y = find(y)
    
    if x == y:
        return False

    if par[x] > par[y]:
        x, y = y, x

    par[x] += par[y]
    par[y] = x
    return True


def size(x):
    '''
    xが属する集合の個数を求める
    '''
    return -par[find(x)]


def same(x, y):
    '''
    xとyが同じ集合に属するかを判定する
    '''
    return find(x) == find(y)



v = 6           # 頂点数
par = [-1] * v  # 根:-size, 葉:親の頂点

'''
union(0, 1)
union(0, 3)
union(1, 4)

find(3)
 > 0

size(1)
> 4

same(1, 3)
> True
'''