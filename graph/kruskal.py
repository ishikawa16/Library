# Kruskal's Algorithm

def kruskal():
    '''
    最小全域木のコストを求める (重み付き無向グラフ)
    O(ElogV)
    '''
    cost = 0
    edge.sort()

    for c, p, q in edge:
        if same(p, q):
            continue
        union(p, q)
        cost += c

    return cost


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


def same(x, y):
    '''
    xとyが同じ集合に属するかを判定する
    '''
    return find(x) == find(y)



v = 6           # 頂点数
par = [-1] * v  # 根:-size, 葉:親の頂点
edge = [[1, 0, 1],
        [3, 0, 2],
        [1, 1, 2],
        [7, 1, 3],
        [1, 2, 4],
        [3, 1, 4],
        [1, 3, 4],
        [1, 3, 5],
        [6, 4, 5]
        ]  # edge[i]:[重み,頂点1,頂点2]

'''
kruskal()
> 5
'''