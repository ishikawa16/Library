class BinaryIndexedTree:
    """BIT: Binary Indexed Tree

    Attributes:
        n (int):     要素数
        data (list): 要素の格納先 (1-indexed)
    """
    def __init__(self, a):
        """初期化 O(NlogN)
    
        Args:
            a (list): 対象の配列
        """
        self.n = len(a)
        self.data = [0] * (self.n + 1)
        for i, v in enumerate(a):
            self.update(i+1, v)

    def query(self, i):
        """区間和の計算 O(logN)

        Args:
            i (int): 区間の右端のindex
        
        Returns:
            int: [0, i)の区間和
        """
        res = 0
        while i > 0:
            res += self.data[i]
            i -= i & -i
        
        return res

    def update(self, i, v):
        """値の更新 O(logN)

        Args:
            i (int): 加算対象のindex+1
            v (int): 加算値
        """
        while i <= self.n:
            self.data[i] += v
            i += i & -i


# Driver Code
if __name__ == "__main__":
    a = [1, 3, 5, 2, 6, 4]
    
    bit = BinaryIndexedTree(a)
    
    print(bit.query(5))

    bit.update(3, 2)
    print(bit.query(5))