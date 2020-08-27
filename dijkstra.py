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



v = 5  # 頂点数
edge = [[[4, 1], [3, 2], [9, 3]],
        [[4, 0], [9, 2]],
        [[3, 0], [9, 1], [2, 3], [5, 4]],
        [[9, 0], [2, 2], [1, 4]],
        [[5, 2], [1, 3]],
        ]  # edge[i]:iを始点に持つ辺の[重み,終点]のリスト

'''
dijkstra(0)
> [0, 4, 3, 5, 6]
'''