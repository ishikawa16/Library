# Prim's Algorithm

from heapq import heappush, heappop


def prim():
    '''
    最小全域木のコストを求める (重み付き無向グラフ)
    O(ElogV)
    '''
    cost = 0
    used = [False] * v
    used[0] = True
    edgelist = []

    for e in edge[0]:
        heappush(edgelist, e)

    while edgelist:
        c, n = heappop(edgelist)
        if used[n]:
            continue
        cost += c
        used[n] = True
        for e in edge[n]:
            if used[e[1]]:
                continue
            heappush(edgelist, e)

    return cost


################################
v, e = map(int, input().split())  # v:頂点数, e:辺の数

edge = [[] for _ in range(v)]  # edge[i]:iを始点に持つ辺の[重み,終点]のリスト
for _ in range(e):
    s, t, d = map(int, input().split())
    edge[s].append([d, t])
    edge[t].append([d, s]) 

print(prim())