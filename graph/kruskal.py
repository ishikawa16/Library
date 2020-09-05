def kruskal():
    """クラスカル法 (重み付き無向グラフ) O(ElogV)

    Vars:
        v (int):     頂点数
        edge (list): 辺に関するリスト (edge[i]:[重み,頂点1,頂点2])

    Returns:
        int: 最小全域木のコスト
    """
    uf = UnionFindTree(v)

    cost = 0
    edge.sort()

    for c, p, q in edge:
        if uf.same(p, q):
            continue
        uf.union(p, q)
        cost += c

    return cost


# kruskalの実行に必要なクラス

class UnionFindTree:
    """Union-Find Tree

    Attributes:
        v (int):    頂点数
        par (list): 要素の格納先
    """
    def __init__(self, v):
        """初期化

        Args:
            v (int): 頂点数
        """
        self.v = v
        self.par = [-1] * self.v

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


    def union(self, x, y):
        """要素の併合 O(1)

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



'''
<使用例>
>>> v = 6
>>> edge = [[1, 0, 1],
            [3, 0, 2],
            [1, 1, 2],
            [7, 1, 3],
            [1, 2, 4],
            [3, 1, 4],
            [1, 3, 4],
            [1, 3, 5],
            [6, 4, 5]
            ]
>>> kruskal()
5
'''