class SegmentTree:
    """
    Segment Tree
    """

    def __init__(self, a):
        """
        配列aで初期化
        ide_ele:単位元
            - RmQ(Range Minimum Query) → inf
            - RMQ(Range Maximum Query) → -1
            - RSQ(Range Sum Query)     → 0
            - RPQ(Range Product Query) → 1
            - RGQ(Range GCD Query)     → 0
        """
        self.n = len(a)
        self.num = (2 ** len(bin(self.n - 1)) - 2)
        self.ide_ele = float('inf')
        self.seg = [self.ide_ele] * (2 * self.num)

        for i in range(self.n):
            self.seg[self.num+i-1] = a[i]    
        for i in range(self.num-2, -1, -1) :
            self.seg[i] = self.segfunc(self.seg[2*i+1], self.seg[2*i+2])

    def segfunc(self, x, y):
        """
        問題に応じて返り値を設定
            - RmQ(Range Minimum Query) → min(x, y)
            - RMQ(Range Maximum Query) → max(x, y)
            - RSQ(Range Sum Query)     → x + y
            - RPQ(Range Product Query) → x * y
            - RGQ(Range GCD Query)     → gcd(x, y)
        """
        return min(x, y)

    def query(self, l, r):
        """
        [l, r)についてsegfuncを適用したものを求める
        O(logN)
        """
        if r <= l:
            return self.ide_ele
        
        l += self.num - 1
        r += self.num - 2
        res = self.ide_ele

        while r - l > 1:
            if l & 1 == 0:
                res = self.segfunc(res, self.seg[l])
            if r & 1 == 1:
                res = self.segfunc(res, self.seg[r])
                r -= 1
            l = l // 2
            r = (r - 1) // 2
        
        if l == r:
            res = self.segfunc(res, self.seg[l])
        else:
            res = self.segfunc(res, self.segfunc(self.seg[l], self.seg[r]))
        
        return res

    def update(self, i, v):
        """
        a[i]の値をvに更新
        O(logN)
        """
        i += self.num - 1
        self.seg[i] = v
        while i:
            i = (i - 1) // 2
            self.seg[i] = self.segfunc(self.seg[i*2+1], self.seg[i*2+2])



'''
<使用例(最小値セグ木)>

>>> a = [3, 1, 7, 4, 9, 2]
>>> st = SegmentTree(a)
>>> st.query(1, 4)
1
>>> st.update(1, 6)
>>> st.query(1, 4)
4
'''