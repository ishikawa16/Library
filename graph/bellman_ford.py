def bellman_ford(s):
    """ベルマンフォード法 (重み付き有向グラフ) O(VE)

    Args:
        s (int): 始点
    
    Vars:
        N (int):     頂点数
        edge (list): 辺に関するリスト (edge[i]: [始点,終点,重み])
    
    Returns:
        list/bool: 始点sから各頂点までの最短距離 (負閉路が存在する場合はFalse)
    """
    dist = [float('inf')] * N
    dist[s] = 0

    for i in range(N):
        update = False
        for p, q, w in edge:
            if dist[p] != float('inf') and dist[q] > dist[p] + w:
                dist[q] = dist[p] + w
                update = True
        if not update:
            break
        if i == N - 1:
            return False

    return dist


# Driver Code
if __name__ == "__main__":
    N = 4
    edge = [[0, 1, 2],
            [0, 2, 3],
            [1, 2, -5],
            [1, 3, 1],
            [2, 3, 2]
            ]
    print(bellman_ford(0))
    # [0, 2, -3, -1]