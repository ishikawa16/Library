def ssc():
    """強連結成分分解 (有向グラフ) O(V+E)

    Vars:
        N (int):         頂点数
        edge (list):     辺に関するリスト (edge[i]:     iを始点に持つ辺の終点のリスト)
        edge_rev (list): 辺に関するリスト (edge_rev[i]: iを終点に持つ辺の始点のリスト)

    Returns:
        list: トポロジカル順序 (閉路が存在する場合はFalse)
    """
    def dfs(now):
        visited[now] = True
        for nxt in edge[now]:
            if not visited[nxt]:
                dfs(nxt)
        order.append(now)


    def dfs_rev(now):
        visited[now] = True
        group.append(now)
        for nxt in edge_rev[now]:
            if not visited[nxt]:
                dfs_rev(nxt)


    order = []
    visited = [False] * N
    for i in range(N):
        if not visited[i]:
            dfs(i)

    components = []
    visited = [False] * N
    for i in order[::-1]:
        if not visited[i]:
            group = []
            dfs_rev(i)
            components.append(group)

    return components


# Driver Code
if __name__ == "__main__":
    N = 7
    edge = [[1],
            [2],
            [0, 3],
            [4],
            [3, 5, 6],
            [],
            []
            ]
    edge_rev = [[2],
                [0],
                [1],
                [2, 4],
                [3],
                [4],
                [4]
                ]
    print(ssc())
    # [[0, 2, 1], [3, 4], [6], [5]]