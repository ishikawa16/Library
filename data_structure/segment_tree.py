class SegmentTree:
    """Segment Tree

    Attributes:
        n (int):       要素数
        num (int):     n以上の最小の2の累乗
        ide_ele (int): 単位元
            - RmQ(Range Minimum Query): inf
            - RMQ(Range Maximum Query): -1
            - RSQ(Range Sum Query):     0
            - RPQ(Range Product Query): 1
            - RGQ(Range GCD Query):     0
        seg (list):    要素の格納先
    """
    def __init__(self, a):
        """初期化 O(N)
        
        Args:
            a (list): 対象の配列
        """
        self.n = len(a)
        self.num = 2 ** (self.n - 1).bit_length()
        self.ide_ele = float('inf')
        self.seg = [self.ide_ele] * (2*self.num)

        for i in range(self.n):
            self.seg[self.num+i-1] = a[i]    
        for i in range(self.num-2, -1, -1) :
            self.seg[i] = self.st_func(self.seg[2*i+1], self.seg[2*i+2])

    def query(self, l, r):
        """区間クエリの計算 O(logN)

        Args:
            l (int): 区間の左端
            r (int): 区間の右端
        
        Returns:
            int: [l, r)についての区間クエリ
        """
        if r <= l:
            return self.ide_ele
        
        l += self.num - 1
        r += self.num - 2
        res = self.ide_ele

        while r - l > 1:
            if l & 1 == 0:
                res = self.st_func(res, self.seg[l])
            if r & 1 == 1:
                res = self.st_func(res, self.seg[r])
                r -= 1
            l = l // 2
            r = (r - 1) // 2
        
        if l == r:
            res = self.st_func(res, self.seg[l])
        else:
            res = self.st_func(res, self.st_func(self.seg[l], self.seg[r]))
        
        return res

    def update(self, i, v):
        """値の更新 O(logN)

        Args:
            i (int): 更新対象のindex
            v (int): 更新値
        """
        i += self.num - 1
        self.seg[i] = v
        while i:
            i = (i - 1) // 2
            self.seg[i] = self.st_func(self.seg[i*2+1], self.seg[i*2+2])
    
    def st_func(self, x, y):
        """問題に応じた処理

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
    a = [2, 5, 3, 8, 7, 0, 9, 1, 6, 4]
    
    st = SegmentTree(a)
    
    print(st.query(1, 7))
    
    st.update(5, 4)
    print(st.query(1, 7))