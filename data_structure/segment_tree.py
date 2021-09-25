class SegmentTree:
    """Segment Tree

    Attributes:
        n (int):       要素数以上の最小の2の累乗
        ide_ele (int): 単位元
            - RmQ (Range Minimum Query): inf
            - RMQ (Range Maximum Query): -1
            - RSQ (Range Sum Query):     0
            - RPQ (Range Product Query): 1
            - RGQ (Range GCD Query):     0
        tree (list):   要素の格納先 (1-indexed)
    """
    def __init__(self, arr):
        """初期化 O(N)

        Args:
            arr (list): 対象の配列
        """
        self.n = 1 << (len(arr)-1).bit_length()
        self.ide_ele = float('inf')
        self.tree = [self.ide_ele] * (2*self.n)

        for i, v in enumerate(arr, self.n):
            self.tree[i] = v
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.seg_func(self.tree[2*i], self.tree[2*i+1])

    def update(self, i, v):
        """値の更新 O(logN)

        Args:
            i (int): 更新対象のindex
            v (int): 更新値
        """
        i += self.n
        self.tree[i] = v
        while i > 1:
            i >>= 1
            self.tree[i] = self.seg_func(self.tree[i*2], self.tree[i*2+1])

    def add(self, i, v):
        """値の加算 O(logN)

        Args:
            i (int): 加算対象のindex
            v (int): 加算値
        """
        i += self.n
        self.tree[i] += v
        while i > 1:
            i >>= 1
            self.tree[i] = self.seg_func(self.tree[i*2], self.tree[i*2+1])

    def query(self, l, r):
        """区間クエリの計算 O(logN)

        Args:
            l (int): 区間の左端
            r (int): 区間の右端

        Returns:
            int: [l, r)についての区間クエリ
        """
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

    def seg_func(self, x, y):
        """問題に応じた処理

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
    A = [2, 5, 3, 8, 7, 1, 9, 0, 6, 4]

    st = SegmentTree(A)

    print(st.query(1, 7))
    # 1

    st.update(5, 4)
    print(st.query(1, 7))
    # 3

    st.add(2, 4)
    print(st.query(1, 7))
    # 4