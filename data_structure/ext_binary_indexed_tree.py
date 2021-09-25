class ExtBinaryIndexedTree:
    """BITを拡張したデータ構造 (k番目に小さい値を高速に取得)

    Attributes:
        n (int):     要素数
        data (list): 要素の格納先 (1-indexed)
    """
    def __init__(self, max_v):
        """初期化 O(1)

        Args:
            max_v (int): 要素の上限値
        """
        self.n = max_v + 1
        self.data = [0] * (max_v+1)

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

    def lower_bound(self, k):
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


# Driver Code
if __name__ == "__main__":
    bit = ExtBinaryIndexedTree(10)

    bit.add(3)            # {3}
    bit.add(1)            # {1, 3}
    bit.add(5)            # {1, 3, 5}
    print(bit.lower_bound(2))
    # 3
    print(bit.search(5))
    # 3

    bit.remove(3)         # {1, 5}
    print(bit.lower_bound(2))
    # 5