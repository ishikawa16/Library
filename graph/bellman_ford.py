def bellman_ford(s):
    """ベルマンフォード法 (重み付き有向グラフ) O(VE)

    Args:
        s (int): 始点
    
    Vars:
        v (int):     頂点数
        edge (list): 辺に関するリスト (edge[i]:[始点,終点,重み])
    
    Returns:
        list/bool: 始点sから各頂点までの最短距離 (負閉路が存在する場合はFalse)
    """
    dist = [float('inf')] * v
    dist[s] = 0

    for i in range(v):
        update = False
        for p, q, cost in edge:
            if dist[p] != float('inf') and dist[q] > dist[p] + cost:
                dist[q] = dist[p] + cost
                update = True
        if not update:
            break
        if i == v - 1:
            return False

    return dist



'''
<使用例>
>>> v = 4
>>> edge = [[0, 1, 2],
            [0, 2, 3],
            [1, 2, -5],
            [1, 3, 1],
            [2, 3, 2]
            ]
>>> bellman_ford(0)
[0, 2, -3, -1]
'''