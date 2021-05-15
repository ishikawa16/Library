import collections

def topological_sort():
    """トポロジカルソート (有向グラフ) O(V+E)

    Vars:
        N (int):     頂点数
        edge (list): 辺に関するリスト (edge[i]: iを始点に持つ辺の終点のリスト)

    Returns:
        list/bool: トポロジカル順序 (閉路が存在する場合はFalse)
    """
    in_degree = [0] * N
    for i in range(N):
        for v in edge[i]:
            in_degree[v] += 1

    nodelist = collections.deque()
    for i in range(N):
        if in_degree[i] == 0:
            nodelist.append(i)

    res = []
    while nodelist:
        p = nodelist.popleft()
        for q in edge[p]:
            in_degree[q] -= 1
            if in_degree[q] == 0:
                nodelist.append(q)

        res.append(p)

    if len(res) == N:
        return res
    else:
        return False


# Driver Code
if __name__ == "__main__":
    N = 6
    edge = [[1],
            [2],
            [],
            [1, 4],
            [5],
            [2]
            ]
    print(topological_sort())
    # [0, 3, 1, 4, 5, 2]