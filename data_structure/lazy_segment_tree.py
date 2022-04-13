class LazySegmentTree:
    """Lazy Segment Tree

    Attributes:
        n (int):       要素数以上の最小の2の累乗
        ide_ele (int): 単位元
            - RmQ (Range Minimum Query): inf
            - RMQ (Range Maximum Query): -1
            - RSQ (Range Sum Query):     0
            - RPQ (Range Product Query): 1
            - RGQ (Range GCD Query):     0
        tree (list):   要素の格納先 (1-indexed)
        lazy (list):   遅延配列 (1-indexed)
            - RUQ (Range Update Query): [None] * (2*self.n)
            - RAQ (Range Add Query):    [0] * (2*self.n)
    """
    def __init__(self, a):
        """初期化 O(N)

        Args:
            a (list): 対象の配列
        """
        self.n = 1 << (len(a)-1).bit_length()
        self.ide_ele = float('inf')
        self.tree = [self.ide_ele] * (2*self.n)
        self.lazy = [None] * (2*self.n)

        for i, v in enumerate(a, self.n):
            self.tree[i] = v
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.seg_func(self.tree[2*i], self.tree[2*i+1])

    def update(self, l, r, v):
        """区間更新 O(logN)

        Args:
            l (int): 区間の左端
            r (int): 区間の右端
            v (int): 更新値
        """
        *ids, = self.index(l, r)
        self.propagate(*ids)

        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                self.tree[l] = v
                self.lazy[l] = v
                l += 1
            if r & 1:
                r -= 1
                self.tree[r] = v
                self.lazy[r] = v
            r >>= 1
            l >>= 1

        for i in ids:
            self.tree[i] = self.seg_func(self.tree[2*i], self.tree[2*i+1])

    def add(self, l, r, v):
        """区間加算 O(logN)

        Args:
            l (int): 区間の左端
            r (int): 区間の右端
            v (int): 更新値
        """
        *ids, = self.index(l, r)

        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                self.tree[l] += v
                self.lazy[l] += v
                l += 1
            if r & 1:
                r -= 1
                self.tree[r] += v
                self.lazy[r] += v
            r >>= 1
            l >>= 1

        for i in ids:
            self.tree[i] = self.seg_func(self.tree[2*i], self.tree[2*i+1]) + self.lazy[i]

    def query(self, l, r):
        """区間クエリの計算 O(logN)

        Args:
            l (int): 区間の左端
            r (int): 区間の右端

        Returns:
            int: [l, r)についての区間クエリ
        """
        *ids, = self.index(l, r)
        self.propagate(*ids)

        l += self.n
        r += self.n
        res = self.ide_ele
        while l < r:
            if l & 1:
                res = self.seg_func(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.seg_func(res, self.tree[r])
            l >>= 1
            r >>= 1

        return res

    def index(self, l, r):
        """伝搬対象の区間の列挙 O(logN)

        Args:
            l (int): 区間の左端
            r (int): 区間の右端

        Yields:
            int: 伝搬対象の区間のindex
        """
        l += self.n
        r += self.n
        l_index = l >> (l&-l).bit_length()
        r_index = r >> (r&-r).bit_length()

        while l < r:
            if l <= l_index:
                yield l
            if r <= r_index:
                yield r
            l >>= 1
            r >>= 1
        while l:
            yield l
            l >>= 1

    def propagate(self, *ids):
        """遅延伝搬処理 O(logN)

        Args:
            ids (tuple): 伝搬対象の区間index
        """
        # RUQ
        for i in reversed(ids):
            if self.lazy[i] is None:
                continue
            self.tree[2*i] = self.lazy[i]
            self.tree[2*i+1] = self.lazy[i]
            self.lazy[2*i] = self.lazy[i]
            self.lazy[2*i+1] = self.lazy[i]
            self.lazy[i] = None

        # RAQ
        # for i in reversed(ids):
        #     if not self.lazy[i]:
        #         continue
        #     self.tree[2*i] += self.lazy[i]
        #     self.tree[2*i+1] += self.lazy[i]
        #     self.lazy[2*i] += self.lazy[i]
        #     self.lazy[2*i+1] += self.lazy[i]
        #     self.lazy[i] = 0

    def seg_func(self, x, y):
        """問題に応じた処理 O(1)

        Args:
            x (int): 左オペランド
            y (int): 右オペランド

        Returns:
            int: 問題に応じた値
                - RmQ(Range Minimum Query): min(x, y)
                - RMQ(Range Maximum Query): max(x, y)
                - RSQ(Range Sum Query):     x + y
                - RPQ(Range Product Query): x * y
                - RGQ(Range GCD Query):     gcd(x, y)
        """
        return min(x, y)


# Driver Code
if __name__ == "__main__":
    A = [2, 5, 3, 8, 7, 0, 9, 1, 6, 4]

    lst = LazySegmentTree(A)

    print(lst.query(1, 7))
    # 0

    lst.update(2, 6, 4)
    print(lst.query(1, 7))
    # 4