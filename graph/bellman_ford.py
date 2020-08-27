# Bellman-Ford Algorithm

def bellman_ford(s):
    '''
    始点sから各頂点への最短距離を求める (重み付き有向グラフ)
    O(VE)
    '''
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
        if i == v - 1:  # 負閉路が存在する場合はFalseを返す
            return False

    return dist



v = 4  # 頂点数
edge = [[0, 1, 2],
        [0, 2, 3],
        [1, 2, -5],
        [1, 3, 1],
        [2, 3, 2]
        ]  # edge[i]:[始点,終点,重み]

'''
bellman_ford(0)
> [0, 2, -3, -1]
'''