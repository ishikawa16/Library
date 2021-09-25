def kruskal():
    """クラスカル法 (重み付き無向グラフ) O(ElogV)

    Vars:
        N (int):     頂点数
        edge (list): 辺に関するリスト (edge[i]: [重み,頂点1,頂点2])

    Returns:
        int: 最小全域木のコスト
    """
    uf = UnionFindTree(N)

    cost = 0
    edge.sort()

    for w, p, q in edge:
        if uf.same(p, q):
            continue
        uf.unite(p, q)
        cost += w

    return cost


# kruskalの実行に必要なクラス
class UnionFindTree:
    """Union-Find Tree

    Attributes:
        n (int):    頂点数
        par (list): 各要素の親要素を格納するリスト
    """
    def __init__(self, n):
        """初期化 O(1)

        Args:
            n (int): 頂点数
        """
        self.par = [-1] * n

    def find(self, x):
        """要素の検索 O(α(N))

        Args:
            x (int): 対象要素

        Returns:
            int: xの根
        """
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        """要素の併合 O(α(N))

        Args:
            x (int): 併合対象の集合に属する要素
            y (int): 併合対象の集合に属する要素
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

    def same(self, x, y):
        """要素の判定 O(1)

        Args:
            x (int): 判定対象の要素
            y (int): 判定対象の要素

        Returns:
            bool: xとyが同じ集合に属するか否か
        """
        return self.find(x) == self.find(y)

    def size(self, x):
        """要素数の計算 O(1)

        Args:
            x (int): 対象要素

        Returns:
            int: xが属する集合の要素数
        """
        return -self.par[self.find(x)]


# Driver Code
if __name__ == "__main__":
    N = 6
    edge = [[1, 0, 1],
            [3, 0, 2],
            [1, 1, 2],
            [7, 1, 3],
            [1, 2, 4],
            [3, 1, 4],
            [1, 3, 4],
            [1, 3, 5],
            [6, 4, 5]
            ]
    print(kruskal())
    # 5