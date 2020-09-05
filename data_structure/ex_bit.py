class ExtBIT:
    """BITを拡張したデータ構造 (k番目に小さい値を高速に取得)

    Attributes:
        n (int):     要素数
        data (list): 要素の格納先 (1-indexed)
    """
    def __init__(self, max):
        """初期化

        Args:
            max (int): 要素の上限値
        """
        self.n = max + 1
        self.data = [0] * (self.n + 1)
    
    def add(self, v):
        """値の追加 O(logN)

        Args:
            v (int): 追加する値
        """
        i = v + 1
        while i <= self.n:
            self.data[i] += 1
            i += i & -i
    
    def remove(self, v):
        """値の削除 O(logN)

        Args:
            v (int): 削除する値
        """
        i = v + 1
        while i <= self.n:
            self.data[i] -= 1
            i += i & -i
    
    def search(self, v):
        """値の検索 O(logN)

        Args:
            v (int): 対象の値
        
        Returns:
            int: vが何番目に小さいか
        """
        i = v + 1
        res = 0
        while i > 0:
            res += self.data[i]
            i -= i & -i
        
        return res
    
    def get(self, k):
        """値の取得 O(logN)

        Args:
            k (int): 何番目に小さい値を取得するか
        
        Returns:
            int: k番目に小さい値
        """
        high = self.n
        low = -1
        while high - low > 1:
            mid = (high + low) // 2

            if self.search(mid) >= k:
                high = mid
            else:
                low = mid
        
        return high



'''
<使用例>
>>> bit = ExtBIT(10)
>>> bit.add(3)
>>> bit.add(1)
>>> bit.add(5)
>>> bit.get(2)
3
>>> bit.search(5)
3
>>> bit.remove(3)
>>> bit.get(2)
5
'''