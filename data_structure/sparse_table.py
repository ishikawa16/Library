class SparseTable:
    """Sparse Table

    Attributes:
        n (int):       要素数
        num (int):     n以上の最小の2の累乗
        ide_ele (int): 単位元
            - RmQ(Range Minimum Query): inf
            - RMQ(Range Maximum Query): -1
            - RGQ(Range GCD Query):     0
        table (list):  要素の格納先
    """
    def __init__(self, a):
        """初期化 O(NlogN)
        
        Args:
            a (list): 対象の配列
        """
        self.n = len(a)
        self.num = (self.n - 1).bit_length()
        self.ide_ele = float('inf')
        self.table = [[self.ide_ele] * self.num for _ in range(self.n)]

        for i in range(self.n):
            self.table[i][0] = a[i]
        
        for k in range(1, self.num):
            for i in range(self.n-2**k+1):
                self.table[i][k] = self.st_func(self.table[i][k-1], self.table[i+2**(k-1)][k-1])
        
    def query(self, l, r):
        """区間クエリの計算 O(1)

        Args:
            l (int): 区間の左端
            r (int): 区間の右端
        
        Returns:
            int: [l, r)についての区間クエリ
        """
        w = r - l

        if w == 1:
            return self.table[l][0]
        else:
            k = ((w+1)//2-1).bit_length()
            return self.st_func(self.table[l][k], self.table[r-2**k][k])
    
    def st_func(self, x, y):
        """問題に応じた処理

        Returns:
            int: 問題に応じた値
                - RmQ(Range Minimum Query): min(x, y)
                - RMQ(Range Maximum Query): max(x, y)
                - RGQ(Range GCD Query):     gcd(x, y)
        """
        return min(x, y)


# Driver Code
if __name__ == "__main__":
    A = [2, 5, 3, 8, 7, 0, 9, 1, 6, 4]

    st = SparseTable(A)

    print(st.query(1, 4))
    # 3
    print(st.query(6, 10))
    # 1
    print(st.query(2, 9))
    # 0