class BinaryIndexedTree:
    """
    BIT: Binary Indexed Tree
    """

    def __init__(self, a):
        """
        配列aで初期化
        """
        self.n = len(a)
        self.data = [0] * (self.n + 1)
        for i, v in enumerate(a):
            self.update(i+1, v)

    def query(self, i):
        """
        a[0] + a[1] + … + a[i-1] を求める
        O(logN)
        """
        res = 0
        while i > 0:
            res += self.data[i]
            i -= i & -i
        
        return res

    def update(self, i, v):
        """
        a[i-1]にvを加算
        O(logN)
        """
        while i <= self.n:
            self.data[i] += v
            i += i & -i



'''
<使用例>

>>> a = [1, 3, 5, 2, 6, 4]
>>> BIT = BinaryIndexedTree(a)
>>> BIT.query(5)
17
>>> BIT.update(3, 2)
>>> BIT.query(5)
19
'''