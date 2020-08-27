# Warshall-Floyd Algorithm

def warshall_floyd():
    '''
    すべての頂点間の最短距離を求める (重み付き有向グラフ)
    O(V^3)
    '''
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist



v = 4  # 頂点数
dist = [[0, 1, 5, float('inf')],
        [float('inf'), 0, 2, 4],
        [float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), 7, 0]
        ]  # dist[i][j]:i→jの重み(存在しない場合はinf, i = jの場合は0)

'''
warshall_floyd()
> [[0, 1, 3, 4],
   [inf, 0, 2, 3],
   [inf, inf, 0, 1],
   [inf, inf, 7, 0]
   ]
'''