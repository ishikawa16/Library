def warshall_floyd():
    """ワーシャルフロイド法 (重み付き有向グラフ) O(V^3)

    Vars:
        n (int):     頂点数
        dist (list): 各頂点間の暫定の最短距離 (dist[i][j]:i→jの重み(存在しない場合はinf, i = jの場合は0))

    Returns:
        list: すべての頂点間の最短距離
    """
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


# Driver Code
if __name__ == "__main__":
    n = 4
    dist = [[0,            1,            5, float('inf')],
            [float('inf'), 0,            2, 4],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), 7, 0]
            ]
    print(warshall_floyd())
    # [[0,   1,   3, 4],
    #  [inf, 0,   2, 3],
    #  [inf, inf, 0, 1],
    #  [inf, inf, 7, 0]
    #  ]