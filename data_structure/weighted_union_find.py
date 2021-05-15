class WeightedUnionFindTree:
    """Weighted Union-Find Tree

    Attributes:
        n (int):       頂点数
        par (list):    要素の格納先
        diff_w (list): 親要素との値の差分
    """
    def __init__(self, n):
        """初期化 O(1)

        Args:
            n (int): 頂点数
        """
        self.par = [-1] * n
        self.diff_w = [0] * n

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
            p = self.find(self.par[x])
            self.diff_w[x] += self.diff_w[self.par[x]]
            self.par[x] = p
            return p

    def weight(self, x):
        """要素の重みの取得 O(1)

        Args:
            x (int): 対象要素

        Returns:
            int: xの根からの距離
        """
        self.find(x)
        return self.diff_w[x]

    def unite(self, x, y, w):
        """要素の併合 O(1)
        
        Args:
            x (int): 併合対象の集合に属する要素
            y (int): 併合対象の集合に属する要素
            w (int): xとyの重みの差分目標 (weight(y) - weight(x))
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

    def diff(self, x, y):
        """重みの差分計算 O(1)

        Args:
            x (int): 対象要素
            y (int): 対象要素

        Returns:
            int: xとyの重みの差分 (weight(y) - weight(x))
        """
        return self.weight(y) - self.weight(x)


# Driver Code
if __name__ == "__main__":
    uf = WeightedUnionFindTree(6)
    
    uf.unite(0, 1, 4)
    uf.unite(0, 3, 6)
    uf.unite(1, 4, 8)
    print(uf.weight(4))
    # 12
    print(uf.diff(1, 3))
    # 2