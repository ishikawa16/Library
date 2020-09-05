import heapq

def prim():
    """プリム法 (重み付き無向グラフ) O(ElogV)

    Vars:
        v (int):     頂点数
        edge (list): 辺に関するリスト (edge[i]:iを始点に持つ辺の[重み,終点]のリスト)

    Returns:
        int: 最小全域木のコスト
    """
    cost = 0
    used = [False] * v
    used[0] = True
    edgelist = []

    for e in edge[0]:
        heapq.heappush(edgelist, e)

    while edgelist:
        c, n = heapq.heappop(edgelist)
        if used[n]:
            continue
        cost += c
        used[n] = True
        for e in edge[n]:
            if used[e[1]]:
                continue
            heapq.heappush(edgelist, e)

    return cost



'''
<使用例>
>>> v = 6
>>> edge = [[[1, 1], [3, 2]], 
            [[1, 0], [1, 2], [7, 3], [3, 4]],
            [[3, 0], [1, 1], [1, 4]],
            [[7, 1], [1, 4], [1, 5]],
            [[3, 1], [1, 2], [1, 3], [6, 5]],
            [[1, 3], [6, 4]]
            ]
>>> prim()
5
'''