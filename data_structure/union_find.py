class UnionFindTree:
    """
    Union-Find Tree
    """

    def __init__(self, v):
        """
        頂点数vで初期化
        """
        self.v = v
        self.par = [-1] * self.v

    def find(self, x):
        """
        xの根を求める
        O(α(N))
        """
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]


    def union(self, x, y):
        """
        xとyの属する集合を併合する
        """
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return

        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        """
        xが属する集合の個数を求める
        """
        return -self.par[self.find(x)]

    def same(self, x, y):
        """
        xとyが同じ集合に属するかを判定する
        """
        return self.find(x) == self.find(y)



'''
<使用例>

>>> uf = UnionFindTree(6)
>>> uf.union(0, 1)
>>> uf.union(0, 3)
>>> uf.union(1, 4)
>>> uf.find(3)
0
>>> uf.size(1)
4
>>> uf.same(1, 3)
True
'''