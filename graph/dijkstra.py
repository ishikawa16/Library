import heapq

def dijkstra(s):
    """ダイクストラ法 (重み付き有向グラフ) O(ElogV)

    Args:
        s (int): 始点

    Vars:
        N (int):     頂点数
        edge (list): 辺に関するリスト (edge[i]: iを始点に持つ辺の[重み,終点]のリスト)

    Returns:
        list: 始点sから各頂点までの最短距離
    """
    dist = [float('inf')] * N
    dist[s] = 0
    edgelist = []
    heapq.heappush(edgelist, [0, s])

    while edgelist:
        w, v = heapq.heappop(edgelist)
        if dist[v] < w:
            continue
        for e in edge[v]:
            if dist[e[1]] <= dist[v] + e[0]:
                continue
            dist[e[1]] = dist[v] + e[0]
            heapq.heappush(edgelist, [dist[e[1]], e[1]])

    return dist


# Driver Code
if __name__ == "__main__":
    N = 5
    edge = [[[4, 1], [3, 2], [9, 3]],
            [[4, 0], [9, 2]],
            [[3, 0], [9, 1], [2, 3], [5, 4]],
            [[9, 0], [2, 2], [1, 4]],
            [[5, 2], [1, 3]],
            ]
    print(dijkstra(0))
    # [0, 4, 3, 5, 6]