class WeightedUnionFindTree:
    """
    Weighted Union-Find Tree
    """

    def __init__(self, v):
        """
        頂点数vで初期化
        """
        self.v = v
        self.par = [-1] * self.v
        self.diff_w = [0] * self.v

    def find(self, x):
        """
        xの根を求める
        O(α(N))
        """
        if self.par[x] < 0:
            return x
        else:
            p = self.find(self.par[x])
            self.diff_w[x] += self.diff_w[self.par[x]]
            self.par[x] = p
            return p

    def weight(self, x):
        """
        xの根からの距離を求める
        """
        self.find(x)
        return self.diff_w[x]

    def union(self, x, y, w):
        """
        weight(y) - weight(x) = w となるようにxとyの属する集合を併合する
        """
        w += self.weight(x) - self.weight(y)
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return

        if self.par[x] > self.par[y]:
            x, y = y, x
            w = -w
        
        self.par[x] += self.par[y]
        self.par[y] = x
        self.diff_w[y] = w

    def same(self, x, y):
        """
        xとyが同じ集合に属するかを判定する
        """
        return self.find(x) == self.find(y)

    def size(self, x):
        """
        xが属する集合の個数を求める
        """
        return -self.par[self.find(x)]

    def diff(self, x, y):
        """
        xとyが同じ集合に属するときの w[y] - w[x] を求める
        """
        return self.weight(y) - self.weight(x)



'''
<使用例>

>>> uf = WeightedUnionFindTree(6)
>>> uf.union(0, 1, 4)
>>> uf.union(0, 3, 6)
>>> uf.union(1, 4, 8)
>>> uf.weight(4)
12
>>> uf.diff(1, 3)
2
'''