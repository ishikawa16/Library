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


################################
v, e = map(int, input().split())  # v:頂点数, e:辺の数

par = [-1] * v  # 根:-size, 葉:親の頂点
edge = []       # edge[i]:[重み,頂点1,頂点2]
for _ in range(e):
    s, t, d = map(int, input().split())
    edge.append([d, s, t])

print(kruskal())