# Dijkstra's Algorithm

from heapq import heappush, heappop


def dijkstra(s):
    '''
    始点sから各頂点への最短距離を求める (重み付き有向グラフ)
    O(ElogV)
    '''
    dist = [float('inf')] * v
    dist[s] = 0
    used = [False] * v
    used[s] = True
    edgelist = []

    for e in edge[s]:
        heappush(edgelist, e)

    while edgelist:
        c, n = heappop(edgelist)
        if used[n]:
            continue
        dist[n] = c
        used[n] = True
        for e in edge[n]:
            if used[e[1]]:
                continue
            heappush(edgelist, [e[0] + dist[n], e[1]])

    return dist


################################
v, e = map(int, input().split())  # v:頂点数, e:辺の数

edge = [[] for _ in range(v)]  # edge[i]:iを始点に持つ辺の[重み,終点]のリスト
for _ in range(e):
    s, t, d = map(int, input().split())
    edge[s].append([d, t])

print(dijkstra(0))