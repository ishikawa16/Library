import heapq

def dijkstra(s):
    """ダイクストラ法 (重み付き有向グラフ) O(ElogV)

    Args:
        s (int): 始点
    
    Vars:
        v (int):     頂点数
        edge (list): 辺に関するリスト (edge[i]:iを始点に持つ辺の[重み,終点]のリスト)
    
    Returns:
        list: 始点sから各頂点までの最短距離
    """
    dist = [float('inf')] * v
    dist[s] = 0
    used = [False] * v
    used[s] = True
    edgelist = []

    for e in edge[s]:
        heapq.heappush(edgelist, e)

    while edgelist:
        c, n = heapq.heappop(edgelist)
        if used[n]:
            continue
        dist[n] = c
        used[n] = True
        for e in edge[n]:
            if used[e[1]]:
                continue
            heapq.heappush(edgelist, [e[0] + dist[n], e[1]])

    return dist


# Driver Code
if __name__ == "__main__":
    v = 5
    edge = [[[4, 1], [3, 2], [9, 3]],
            [[4, 0], [9, 2]],
            [[3, 0], [9, 1], [2, 3], [5, 4]],
            [[9, 0], [2, 2], [1, 4]],
            [[5, 2], [1, 3]],
            ]
    print(dijkstra(0))
    # [0, 4, 3, 5, 6]