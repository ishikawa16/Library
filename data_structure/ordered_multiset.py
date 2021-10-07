class OrderedMultiset:
    """順序付き多重集合

    Attributes:
        n (int):     要素数
        data (list): 要素の格納先 (1-indexed)
    """
    def __init__(self, max_v):
        """初期化 O(1)

        Args:
            max_v (int): 要素の上限値
        """
        self.n = max_v
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

    def lower_bound(self, v):
        """値の取得 O(logN)

        Args:
            v (int): 対象の値

        Returns:
            int: vより大きい要素のうち最小の要素
        """
        k = self.search(v)
        return self.get(k+1)


# Driver Code
if __name__ == "__main__":
    multiset = OrderedMultiset(10)

    multiset.add(3)            # {3}
    multiset.add(1)            # {1, 3}
    multiset.add(4)            # {1, 3, 4}
    multiset.add(7)            # {1, 3, 4, 7}
    multiset.add(4)            # {1, 3, 4, 4, 7}
    print(multiset.get(2))
    # 3
    print(multiset.lower_bound(5))
    # 7

    multiset.remove(3)         # {1, 4, 4, 7}
    print(multiset.get(2))
    # 4